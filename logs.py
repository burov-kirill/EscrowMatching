import logging

logging.basicConfig(filename="logging.log", level=logging.INFO, filemode="w")

log = logging.getLogger("user_log")


def write_control_values(bank, account, count_doc, bank_counted, account_counted):
    if (round(bank - bank_counted, 0) != 0 and round(account - account_counted, 0) != 0):
        log.info(
            f'Входные суммы по банку и БИТ не равны рассчитанным!\n{get_log_string(bank, account, bank_counted, account_counted, count_doc)}')
    elif (round(bank - bank_counted, 0) == 0 and round(account - account_counted, 0) == 0):
        log.info(
            f'Входные суммы по банку и БИТ равны рассчитанным!\n{get_log_string(bank, account, bank_counted, account_counted, count_doc)}')

    elif round(bank- bank_counted, 0) != 0:
        log.info(
            f'Входные суммы по банку не равны рассчитанным!\n{get_log_string(bank, account, bank_counted, account_counted, count_doc)}')
    else:
        log.info(
            f'Входные суммы по БИТ не равны рассчитанным!\n{get_log_string(bank, account, bank_counted, account_counted, count_doc)}')



def get_log_string(bank, account, bank_counted, account_counted, count_doc):
        log_string  =    f'Сумма по входящему банковскому файлу: {bank}\n' \
                         f'Сумма по обработанному банковскому файлу: {bank_counted}\n' \
                         f'Сумма по входящему бухгалтерскому файлу: {account}\n' \
                         f'Сумма по обработанному бухгалтерскому файлу: {account_counted}\n' \
                         f'Количество прочитанных банковских файлов: {count_doc}'
        return log_string
