import pandas as pd
from settings.classes.account import AccountFile
from settings.classes.bank import BankFile
from user_settings.user_interfaces import user_action

pd.options.mode.chained_assignment = None

def start():
    data = user_action()
    user_data = data
    path = user_data['save_to']
    account_data = AccountFile(user_data)
    bank_data = BankFile(user_data, account_data.type_dict)
    return (bank_data, account_data, path)


