from logs import log, write_control_values
from settings.functions.decorating import decoration
from settings.functions.editing import find_matches
from settings.functions.preprocessing import start
from settings.user_settings.user_interfaces import end_panel, error_panel

if __name__ == "__main__":
        try:
                bank_data, account_data, save_path = start()
                matches, review, review_for_MSFO, one_more_review, contract_review = find_matches(account_data, bank_data)
                control_bank_sum, control_account_sum = decoration(matches, review, review_for_MSFO, one_more_review, contract_review, save_path)
                write_control_values(bank_data.document_sum, account_data.document_sum,
                                     bank_data.count_documents, control_bank_sum, control_account_sum)
                end_panel(save_path)

        except Exception as exp:
                log.exception(exp)
                log.info('Авариный выход из программы')
                if error_panel('Непредвиденная ошибка. Описание можно посмотерть в лог файле'):
                        start()







