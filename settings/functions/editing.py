import re
from copy import copy
import pandas as pd

pd.options.mode.chained_assignment = None
from logs import log

dict_columns = {12: ['Контрагент', 'Договор', 'Номер счета', 'Сальдо'],
                11: ['Договор', 'Номер счета', 'Сальдо'], 10: ['Контрагент', 'Номер счета', 'Договор'], 9: ['Контрагент', 'Номер счета', 'Сальдо'],
                8: ['Контрагент', 'Договор', 'Сальдо'], 7: ['Договор', 'Номер счета'], 6: ['Договор', 'Сальдо'],
                5: ['Контрагент', 'Договор'], 4: ['Контрагент', 'Номер счета'], 3: ['Контрагент', 'Сальдо'], 2: ['Номер счета', 'Сальдо'], 1: []}



def create_reaview(bank, account):
    bank["Сальдо"] = pd.to_numeric(bank["Сальдо"], errors='ignore')
    account["Сальдо"] = pd.to_numeric(account["Сальдо"], errors='ignore')
    bank = bank[['Очередь', 'Дом', 'Сальдо']]
    account = account[['Очередь', 'Дом', 'Сальдо']]

    bank = bank.groupby(['Очередь', 'Дом'], as_index=False).agg(sum)
    account = account.groupby(['Очередь', 'Дом'], as_index=False).agg(sum)

    bank.rename(columns={'Сальдо': 'Сальдо_Банк'}, inplace=True)
    account.rename(columns={'Сальдо': 'Сальдо_1C'}, inplace=True)
    result = pd.concat([bank, account])
    result.fillna(0, inplace=True)
    result = result.groupby(['Очередь', 'Дом'], as_index= False).agg(sum)
    result['Разница'] = result['Сальдо_Банк'] - result['Сальдо_1C']
    last_row = {'Очередь': 'ИТОГО', 'Дом': '', 'Сальдо_Банк': result['Сальдо_Банк'].sum(), 'Сальдо_1C':result['Сальдо_1C'].sum(), 'Разница': result['Разница'].sum()}
    result = pd.concat([result, pd.DataFrame(last_row, index=[0])])
    return result

def create_review_for_MSFO(bank, account):
    bank_data = copy(bank.df)
    account_data = copy(account.df)
    bank_data["Сальдо"] = pd.to_numeric(bank_data["Сальдо"], errors='ignore')
    # bank_data["Сумма по ДДУ"] = pd.to_numeric(bank_data["Сумма по ДДУ"], errors='ignore')

    # добавить ответвление на случай если не будет столбца Сумма по ДДУ
    bank_data = bank_data[['Очередь', 'Дом', "Сальдо", 'Сумма по ДДУ']]
    result = bank_data.groupby(['Очередь', 'Дом'], as_index=False).agg(sum)
    if 'Сумма по ДДУ' in account_data.columns:
        result.drop(['Сумма по ДДУ'], axis = 1, inplace=True)
        # Убрать у банка этот столбец
        # result but not mrg_data
        account_data = account_data[['Очередь', "Дом", "Сумма по ДДУ"]]
        account_data = account_data.groupby(['Очередь', 'Дом'], as_index=False).agg(sum)
        result = pd.merge(result, account_data, how='left', left_on=['Очередь', 'Дом'], right_on=['Очередь', 'Дом'])
        result.fillna(0, inplace=True)

    result['% оплаты'] = result['Сальдо']/result['Сумма по ДДУ']
    result['% оплаты'].astype(float).round(4)
    # result = result[['Очередь', 'Дом', 'Сальдо']]
    result = result[['Очередь', 'Дом', 'Сальдо', 'Сумма по ДДУ', '% оплаты']]
    # last_row = {'Очередь': 'ИТОГО', 'Дом': '', 'Сальдо': result['Сальдо'].sum()}
    last_row = {'Очередь': 'ИТОГО','Дом': '', 'Сальдо': result['Сальдо'].sum(), 'Сумма по ДДУ': result['Сумма по ДДУ'].sum(),
                '% оплаты': round(result['Сальдо'].sum()/result['Сумма по ДДУ'].sum(),4)}
    result = pd.concat([result, pd.DataFrame(last_row, index=[0])])
    return result

def create_one_more_review_for_MSFO(bank):
    bank_data = copy(bank.df)
    bank_data["Сальдо"] = pd.to_numeric(bank_data["Сальдо"], errors='ignore')
    bank_data['Очередь'] = bank_data['Договор'].apply(find_queries)
    bank_data['Дом'] = bank_data['Договор'].apply(find_queries, args=[False])
    result = bank_data.groupby(['Очередь', 'Дом'], as_index=False).agg(sum)
    result = result[['Очередь', 'Дом', 'Сальдо']]
    last_row = {'Очередь': 'ИТОГО', 'Дом': '', 'Сальдо': result['Сальдо'].sum()}
    result = pd.concat([result, pd.DataFrame(last_row, index=[0])])
    return result

def fill_df_with_dict(row, esc_dict):
    if row['Номер счета'] == '0':
        tpl_data = (row['Контрагент'], row['Договор'])
        match_acc = esc_dict.get(tpl_data, '0')
        if match_acc != '0':
            return f'!BLUE_{match_acc}'
        else:
            return match_acc
    else:
        return row['Номер счета']
def edit_acc_escrow(acc_data, bank_data):
    bank_data = bank_data[['Контрагент', 'Договор', 'Номер счета']]
    escrow_dict = {(row['Контрагент'], row['Договор']): row['Номер счета'] for (index, row) in bank_data.iterrows()}
    acc_data['Номер счета'] = acc_data.apply(fill_df_with_dict, axis = 1, args=[escrow_dict])
    return acc_data


def find_matches(account, bank):
    log.info(f'Начало процедуры нахождения соответствий в файлах')
    result_dict = dict()
    account_data = copy(account.df)
    bank_data = copy(bank.df)
    account_data = edit_acc_escrow(account_data, bank_data)
    account_data['Очередь_Дом'] = account_data['Очередь'] + "_" + account_data['Дом']
    bank_data['Очередь_Дом'] = bank_data['Очередь'] + "_" + bank_data['Дом']
    query_house_frame = list(map(lambda x: x[0] + '_' + x[1], get_house_and_query_list(bank_data,account_data)))
    query_house_frame.append('Общий')
    review = create_reaview(bank_data, account_data)
    review_for_MSFO = create_review_for_MSFO(bank, account)
    one_more_review = create_one_more_review_for_MSFO(bank)
    for i, row in enumerate(query_house_frame, 1):
        if row != 'Общий':
            temp_bank = bank_data.query("Очередь_Дом == @row")
            temp_account = account_data.query("Очередь_Дом == @row")
            excel_dict = dict()
            bank_data = bank_data.query("Очередь_Дом != @row")
            account_data = account_data.query("Очередь_Дом != @row")
        else:
            excel_dict = dict()
            temp_bank = bank.df
            temp_account = account.df
            temp_account = edit_acc_escrow(temp_account, temp_bank)
        for key, value in sorted(dict_columns.items(), reverse=True):
            if key != 1:
                temp_df = pd.merge(temp_account, temp_bank, how='inner', left_on=value, right_on=value)
                bank_indexes = list(temp_df['bank_id'])
                account_indexes = list(set(list(temp_df['account_id'])))
                excel_dict[key] = (temp_bank.query("bank_id in @bank_indexes"), temp_account.query("account_id in @account_indexes"))
                temp_bank = temp_bank.query("bank_id not in @bank_indexes")
                temp_account = temp_account.query("account_id not in @account_indexes")
            else:
                excel_dict[1] = (temp_bank, temp_account)
        name = row if len(row) > 10 else row[:6]
        result_dict[name] = excel_dict

    return (result_dict, review, review_for_MSFO, one_more_review, bank.contract_review)

def get_house_and_query_list(bank, account):
    short_bank = bank[['Очередь','Дом']]
    short_account = account[['Очередь', 'Дом']]
    common_frame = pd.concat([short_bank, short_account])
    common_frame = common_frame.groupby(['Очередь', 'Дом'], as_index=False).count()
    return list(set(map(tuple, common_frame.values.tolist())))


def find_queries(string, option=True):
    numbers = re.findall(r'(\d+\.?\d*)', string)
    if len(numbers) >= 2:
        if option:
            return numbers[0]
        else:
            return numbers[1]
    else:
        return 'бн'