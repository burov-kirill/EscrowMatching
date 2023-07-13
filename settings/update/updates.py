import time

import requests as requests
from settings.update.config import VERSION_URL, VERSION
from settings.user_settings.user_interfaces import web_error_panel


def get_latest_version():
    error_report = False
    desc = ''
    for _ in range(10):
        try:
            res = requests.get(VERSION_URL)
            time.sleep(2)
            if res.status_code == 200:
                return res.text.split('\n')[-1]
        except Exception as exp:
            error_report = True
            desc = exp
    if error_report:
        web_error_panel(desc)

def check_version():
    latest_version = get_latest_version()
    if VERSION == latest_version:
        return True
    else:
        return False