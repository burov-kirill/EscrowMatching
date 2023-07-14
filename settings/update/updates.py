import subprocess
import threading
import time
import os
import PySimpleGUI as sg
import requests
import sys
from pathlib import Path
from settings.update.config import VERSION_URL, VERSION,  UPDATE_URL, APP_URL, APP_NAME, ZIP_URL, UPDATE_NAME, UPDATE_FOLDER
def web_error_panel(desc):
    event = sg.popup_ok(f'При загрузке данных возникла ошибка: {desc}',
                     background_color='#007bfb', button_color=('white', '#007bfb'),
                     title='Ошибка загрузки')
    if event == 'OK':
        sys.exit()

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

def killProcess(pid):
    subprocess.Popen('taskkill /F /PID {0}'.format(pid, shell=True))

def is_directory():
    path = os.path.dirname(sys.executable)
    onlyfiles = [f[f.rfind('.')+1:] for f in os.listdir(path) if os.path.isfile(os.path.join(path, f))]
    if any(map(lambda x: x == 'pyd', onlyfiles)):
        return True
    else:
        return False
def download_file(window, APP_URL, APP_NAME):
    # auth = (LOGIN, ACCESSTOKEN)
    # with urllib.request.urlopen(APP_URL, context=context) as r:
    with requests.get(APP_URL, stream=True) as r:
        chunk_size = 64*1024
        total_length = int(r.headers.get('content-length'))
        total = total_length//chunk_size if total_length % chunk_size == 0 else total_length//chunk_size + 1
        with open(APP_NAME, 'wb') as f:
            for i, chunk in enumerate(r.iter_content(chunk_size=chunk_size)):
                f.write(chunk)
                PERCENT = int((i+1)/total*100)
                window.write_event_value('Next', PERCENT)


def create_download_window(APP_URL, APP_NAME):
    progress_bar = [
        [sg.ProgressBar(100, size=(40, 20), pad=(0, 0), key='Progress Bar', border_width = 0),
         sg.Text("  0%", size=(4, 1), key='Percent', background_color='#007bfb', border_width=0), ],
    ]

    layout = [
        [sg.pin(sg.Column(progress_bar, key='Progress', visible=True, background_color='#007bfb',
                          pad=(0, 0), element_justification='center'))],
    ]
    window = sg.Window('Загрузка', layout, size=(600, 40), finalize=True,
                       use_default_focus=False, background_color='#007bfb')
    progress_bar = window['Progress Bar']
    percent = window['Percent']
    # progressB = window['Progress']
    default_event = True
    while True:
        event, values = window.read(timeout=10)
        if event == sg.WINDOW_CLOSED:
            break
        elif default_event:
            default_event = False
            progress_bar.update(current_count=0, max=100)
            thread = threading.Thread(target=download_file, args=(window, APP_URL, APP_NAME), daemon=True)
            thread.start()
        elif event == 'Next':
            count = values[event]
            progress_bar.update(current_count=count)
            percent.update(value=f'{count:>3d}%')
            window.refresh()
            if count == 100:
                time.sleep(1)
                break
    window.close()


def get_subpath(path, i):
    while i > 0:
        path = path[:path.rfind('\\')]
    return path

def set_update_params(updater_path, is_dir, type_file):
    PATH = os.path.dirname(sys.executable)
    pid = str(os.getpid())
    FNULL = open(os.devnull, 'w')
    if type_file == 'pocket':
        URL =  ZIP_URL
    else:
        URL = APP_URL
    APP = APP_NAME
    args = f'{updater_path} -config ' + URL + " " + APP + " " + pid + " " + PATH + " " + str(is_dir)
    subprocess.call(args, stdout=FNULL, stderr=FNULL, shell=False)

def call_updater(type_file):
    path = os.path.abspath(__file__).replace(os.path.basename(__file__), '')
    # path = path[:path.rfind('//')]
    is_dir = is_directory()
    if not is_dir:
        os.mkdir(UPDATE_FOLDER)
        upd_path = f'{UPDATE_FOLDER}/{UPDATE_NAME}'
        create_download_window(UPDATE_URL, upd_path)
        set_update_params(upd_path, is_dir, type_file)

    else:
        path = get_subpath(path, 2)
        folder_path = f'{path}\\config'
        my_file = Path(f"{folder_path}\\updater.exe")
        if os.path.isdir('config'):
            if my_file.is_file():
                set_update_params(str(my_file), is_dir, type_file)
            else:
                create_download_window(UPDATE_URL, str(my_file))
                set_update_params(str(my_file), is_dir, type_file)
        else:
            create_download_window(UPDATE_URL, str(my_file))
            set_update_params(str(my_file), is_dir, type_file)