import re

import numpy as np
import openpyxl
import pandas as pd

from logs import log
from user_settings.user_exceptions import PatternColumnsError, DifferentLengthError, WorkbookFilterError
from user_settings.user_interfaces import check_query_panel


class AccountFile:
    TYPE_DOC = 1
    COL_PATTERN = {
        1: ['Тип', 'Договор', 'Контрагент', 'Номер счета'],
        0: ['Тип', 'Договор', 'Контрагент']
    }
    COLUMN_PATTERNS = {
        (str, str, str, np.float64, str): ('new', ['Полный договор', "Контрагент", "Договор", "Сальдо", 'Тип']),
        (str, str, str, np.float64, str): ('new', ['Полный договор', "Контрагент", "Договор", "Сальдо", 'Тип']),
        (str, str, str, np.float64, np.float64, str): (
        'new', ['Полный договор', "Контрагент", "Договор", "Оборот", "Сальдо", 'Тип']),
        (str, str, np.float64, str): ('old', ['Договор', "Контрагент", "Сальдо", 'Тип']),
        (str, str, np.float64, np.float64, str): ('old', ['Договор', "Контрагент", "Оборот", "Сальдо", 'Тип'])}

    def __init__(self, user_data_dict):
        self.name_account_file = user_data_dict['account']
        self.check_nomenclature = user_data_dict['check_nomenclature']
        self.is_check_account = user_data_dict['check_account']
        self.file_to_bank = user_data_dict['file_to_bank']
        self.values_dict = dict()
        self.is_change_group = False
        if len(user_data_dict['bank_name']) > 0:
            self.bank_name = user_data_dict['bank_name'][0]
        else:
            self.bank_name = ''
        self.df = self.create_and_edit_account_dataframe()
        self.type_dict = self.create_type_dict()


    def create_and_edit_account_dataframe(self):
        self.df = self.edit(self.name_account_file, self.bank_name)
        self.set_index_on_df()
        return self.df

    def edit(self, filename, bank_name):
        log.info(f'Считывание файла {filename}')
        try:
            wb = openpyxl.load_workbook(filename)
        except WorkbookFilterError as exp:
            raise WorkbookFilterError(filename)
        raw_data = wb[wb.sheetnames[0]]
        data = self.edit_account_data(raw_data, bank_name)
        wb.close()
        return data

    def edit_account_data(self, raw_account_data, bank_name):
        # if self.type_of_file == False:
        #     merged_celles = []
        #     for cell in raw_account_data.merged_cells.ranges:
        #         if cell.coord.split(':')[0][0]=='A' and cell.coord.split(':')[1][0]=='C':
        #             merged_celles.append(cell.coord.split(':')[0])
        # else:
        merged_celles = list(map(lambda x: x.coord.split(':')[0], raw_account_data.merged_cells.ranges))

        projects = []
        for row in raw_account_data:
            if row[0].coordinate in merged_celles:
                projects.append(row[0].value)
        projects = projects[projects.index('009.СЭ') + 1:projects.index('Итого')]
        row_indexes = []
        headers_list = []
        j = 0
        prj = ''
        for i, row in enumerate(raw_account_data):
            # column = 1 if self.type_of_file else 2
            column = 1
            if sum(map(lambda x: x.value is not None, row)) not in (3, 4, 5, 6, 7, 8, 9) or row[column].value is None:
                if row[0].value == '<...>' and row[0].coordinate not in merged_celles:
                    headers_list.append((j, prj))
                    j += 1
                elif row[0].value in projects and row[0].coordinate in merged_celles:
                    prj = row[0].value
                    row_indexes.append(i)
                else:
                    row_indexes.append(i)
            else:
                headers_list.append((j, prj))
                j += 1
        # col_indexes = []
        account = pd.DataFrame(raw_account_data.values)
        account.drop(row_indexes, inplace=True)
        #
        # for i, col in enumerate(account.columns):
        #     if sum(map(lambda x: x is None, account[col])) > sum(map(lambda x: x is not None, account[col])):
        #         col_indexes.append(i)
        account.reset_index(inplace=True)
        str_col = [col for col in account.columns if account[col][0]!=None and col !='index']
        str_col.append(account.columns[-2])
        account = account[str_col]

        # account.drop(col_indexes, axis=1, inplace=True)
        # account.reset_index(inplace=True)
        # account.drop('index', axis=1, inplace=True)
        prj_df = pd.DataFrame(headers_list, columns=['index', 'prj'])
        prj_df.set_index('index', inplace=True)

        account_data = self.get_projects_name_for_account_data(account, prj_df)
        account_data['Договор'] = account_data['Договор'].apply(lambda x: 'бн' if 'б/н' in str(x) else str(x))
        account_data.sort_values(by=['Договор'], inplace=True)
        # account_data = account_data[['Тип', 'Договор', 'Контрагент', 'Сальдо']]
        account_data['Контрагент'] = account_data['Контрагент'].apply(lambda x: x.strip() if type(x) == str else x)
        account_data["Сальдо"] = pd.to_numeric(account_data["Сальдо"], errors='ignore')
        account_data["Сумма по ДДУ"] = pd.to_numeric(account_data["Сумма по ДДУ"], errors='ignore')
        account_data = account_data.groupby(self.COL_PATTERN[self.TYPE_DOC], as_index=False).agg(sum)
        account_data['account_id'] = range(1, len(account_data) + 1)
        self.document_sum = self.sum_amount(account_data)
        account_data['Сальдо'] = account_data['Сальдо'].apply(str)

        if bank_name == 'Совкомбанк' or 'Совкомбанк' in list(map(lambda x: x[1], self.file_to_bank.values())):
            account_data['Контрагент'] = account_data['Контрагент'].apply(self.edit_account_agent)

        if self.check_nomenclature:
            account_data['Очередь'] = account_data['Тип'].apply(self.get_query)
            account_data['Дом'] = account_data['Тип'].apply(self.get_house)
        else:
            account_data['Очередь'] = account_data['Договор'].apply(self.get_query)
            account_data['Дом'] = account_data['Договор'].apply(self.get_house, args=[False])
            account_data = self.check_data(account_data)

        if self.is_check_account:
            query_house_dict = self.create_query_house_dict(account_data)
            correct_values_dict = check_query_panel(query_house_dict, 'ОСВ')
            self.values_dict = correct_values_dict
            account_data['Очередь'] = account_data['Тип'].apply(self.set_correct_query, args=[correct_values_dict])
            account_data['Дом'] = account_data['Тип'].apply(self.set_correct_house, args=[correct_values_dict])

        account_data['Договор'] = account_data['Договор'].apply(lambda x: str(x).upper())
        return account_data
    def check_data(self, acc):
        if len(acc['Тип'].drop_duplicates()) < len(acc['Дом'].drop_duplicates()):
            self.is_change_group = True
            acc['Тип'] = acc['Тип'] + '_' + acc['Очередь'] + '_' + acc['Дом']
            return acc
        else:
            return acc

    def create_query_house_dict(self, df):
            result = dict()
            df = df.groupby(['Тип', 'Очередь', 'Дом'], as_index=False).count()
            for i in range(len(df)):
                result[df['Тип'][i]] = ((df['Очередь'][i], df['Дом'][i]))
            return result

    @staticmethod
    def set_correct_query(stirng, correct_dict):
        return correct_dict[stirng][0]

    @staticmethod
    def set_correct_house(stirng, correct_dict):
        return correct_dict[stirng][1]

    @staticmethod
    def get_query(string):
        # pattern = r'(?<!-)(\d+[.,]?\d{0,2})'
        pattern = r'\d+[.-]?\d{0,2}'
        parse_str = re.findall(pattern, string)
        if len(parse_str)>=2:
            return parse_str[0]
        else:
            return string

    @staticmethod
    def get_house(string, option = True):
        # pattern = r'(?<!-)(\d+[.,]?\d{0,2})'
        pattern = r'\d+[.-]?\d{0,2}'
        parse_str = re.findall(pattern, string)
        if len(parse_str)>=2:
            if option:
                return parse_str[-1]
            else:
                return parse_str[1]
        else:
            return string

    def create_type_dict(self):
        result = dict()
        temp = self.df[['Очередь', 'Дом']]
        temp = temp.values.tolist()
        temp = list(map(lambda x: tuple(x), temp))
        temp = list(set(temp))
        for element in temp:
            result[element[1]] = element[0]
        return result


    def get_projects_name_for_account_data(self, account, projects):
        if len(projects) == len(account):
            account = pd.merge(account, projects, how='inner', left_index=True, right_index=True)
        else:
            log.exception(DifferentLengthError)
            raise DifferentLengthError
        account = account.fillna(0)
        if len(account.columns) == 5:
            self.TYPE_DOC = 1
            account.columns = ['Полный договор', "Контрагент", "Договор", "Сальдо", 'Тип']
            account['Сумма по ДДУ'] = 0
            account['Номер счета'] = ''
        else:
            account.columns = ['Полный договор', "Контрагент", "Договор", "Номер счета", "Сумма по ДДУ", "Сальдо", 'Тип']
            account['Номер счета'] = account['Номер счета'].apply(str)
        account.drop(index=0, axis=0, inplace=True)
        # columns_types = tuple(map(type, account.iloc[0]))
        # succes_tag = False
        # for key, value in self.COLUMN_PATTERNS.items():
        #     if key == columns_types:
        #         succes_tag = True
        #         account.columns = value[1]
        #         if value[0] == 'new':
        #             account.drop(index=0, axis=0, inplace=True)
        #         if value[0] == 'old':
        #             account['Договор'] = account['Договор'].apply(self.get_contract)
        #         break
        #
        # if not succes_tag:
        #     log.exception(PatternColumnsError)
        #     raise PatternColumnsError(columns_types, account.columns)
        return account

    def get_contract(self, row: str) -> str:
        temp_data = row.split(' ')
        if len(temp_data) > 2:

            return temp_data[0].strip()
        else:

            return row

    def split_contract(self, elem):
        if len(elem.split(' ')) > 1:
            return elem.split(' ')[1]
        else:
            return elem

    def edit_account_agent(self, agent):
        agent_list = str(agent).split(' ')
        if len(agent_list) == 3:
            return f'{agent_list[0].upper()} {agent_list[1][0]}.{agent_list[2][0]}.'
        else:
            return agent

    def set_index_on_df(self):
        self.df['account_id'] = range(1, len(self.df) + 1)

    @staticmethod
    def sum_amount(df):
        result = sum([float(elem) if elem != '' else 0 for elem in df['Сальдо']])
        log.info(f'Сумма по данному документу: {result}')
        return result

