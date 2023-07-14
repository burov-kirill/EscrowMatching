import os
import sys
import time
from glob import glob
import win32com.client
import io
import PySimpleGUI as sg
from PIL import Image

from settings.update.updates import check_version, call_updater


def resource_path(relative_path):
    try:
        base_path = sys._MEIPASS
    except Exception:
        base_path = os.path.abspath("")

    return os.path.join(base_path, relative_path)

image_path = resource_path("samolet.png")

img = Image.open(image_path)
img_resized = img.resize((400, 100))
img_byte_arr = io.BytesIO()
img_resized.save(img_byte_arr, format='png', subsampling=0, quality=100)
img_byte_arr = img_byte_arr.getvalue()
BANK_NAMES = ['СБЕР', 'Альфа Банк', 'Совкомбанк', 'Дом РФ', 'МКБ', 'ВТБ', 'ГПБ', 'ПСБ', "ВБРР", "Промсвязьбанк"]

def user_action():
    values = first_panel()
    files_list = {y[y.rfind('\\') + 1:]: y for x in os.walk(values['bank_folder']) for y in
                  glob(os.path.join(x[0], '*.xlsx'))}
    result = dict()
    check_result = check_user_values(values)
    if check_result == True:
        if values['bank_folder']!='':
            if values['single']:
                result = {key: (value, values['bank_name'][0]) for key, value in files_list.items()}
            else:
                event, new_values = second_panel(files_list)
                if event=='Cancel':
                    return user_action()
                else:
                    for k, v in new_values.items():
                        new_values[k] = v[0]
                    result = {key: (value, new_values[key]) for key, value in files_list.items()}
    else:
        return_to_panel = error_panel(check_result)
        if return_to_panel:
            return user_action()
    values['file_to_bank'] = result
    return values



def first_panel():
    tooltip_bank = 'Если необходимо редактировать номенклатурные группы в банковской ведомости'
    tooltip_account = 'Если необходимо редактировать номенклатурные группы в ОСВ'
    tooltip_redaction = 'Если номенклатурные группы следует искать названии договора в ОСВ'
    tooltip_type = 'Если в ОСВ дата договора и номер не разделены, то снимите галочку'
    yeet = sg.Window('Сверка Банка и ОСВ ver.1.0', background_color='#007bfb').Layout(
        [
            [sg.Image(source = img_byte_arr)],
            [sg.Text('Выберите тип банка', pad=(3,3), background_color='#007bfb'),
             sg.Listbox(values=BANK_NAMES, select_mode = 'LISTBOX_SELECT_MODE_SINGLE', key='bank_name', size=(30, 8))],
            [sg.Text('Доступно обновление',visible=False, key='upd_txt'), sg.Button('Обновить', visible=False, key='upd_btn')],
            [sg.Button('Пакет', visible=False, key='pocket'), sg.Button('Файл', visible=False, key='file')],
            [sg.Text('Выбрать файл данных банка', background_color='#007bfb')],
            [sg.Input(key='bank_file'), sg.FileBrowse()],
            [sg.Text('Выбрать папку с данными банка', background_color='#007bfb')],
            [sg.Input(key='bank_folder'), sg.FolderBrowse()],
            [sg.Text('Выбрать файл с ОСВ', background_color='#007bfb')],
            [sg.Input(key='account'), sg.FileBrowse()],
            [sg.Text('Папка для сохранения файла', background_color='#007bfb')],
            [sg.Input(key='save_to'), sg.FolderBrowse()],
            [sg.Checkbox('ОСВ нового типа', key='type', default=True, tooltip=tooltip_type, background_color='#007bfb')],
            [sg.Text('Настройка параметров обработки', pad=(3, 3), auto_size_text=True,
                     relief='solid', background_color='#007bfb')],
            [sg.Radio('Банковские ведомости от одного банка', "RADIO1", default=True, key='single', background_color='#007bfb')],
            [sg.Radio('Банковские ведомости от разных банков', "RADIO1", default=False, background_color='#007bfb')],
            [sg.Text('Настройка параметров для ревью', justification='center',
                     relief = 'solid', background_color='#007bfb')],
            [sg.Checkbox('Включить функцию редактирования очередь/дом для Банка', key='check', default=True, tooltip=tooltip_bank, background_color='#007bfb')],
            [sg.Checkbox('Включить функцию редактирования очередь/дом для ОСВ', key='check_account', default=False, tooltip=tooltip_account, background_color='#007bfb')],
            [sg.Checkbox('Редакция ОСВ по номенклатуре', key='check_nomenclature', default=True, tooltip=tooltip_redaction, background_color='#007bfb')],

            [sg.OK(), sg.Cancel()]
        ])
    upd_check = check_version()
    # if not upd_check:
    #     yeet['upd_txt'].Update(visible=True)
    #     yeet['upd_btn'].Update(visible=True)
    while True:
        event, values = yeet.Read(timeout=10)
        if not upd_check:
            yeet['upd_txt'].Update(visible=True)
            yeet['upd_btn'].Update(visible=True)
        if event == 'upd_btn':
            yeet['pocket'].Update(visible=True)
            yeet['file'].Update(visible=True)
        if event in ('pocket', 'file'):
            call_updater(event)
        if event == 'Cancel':
            sys.exit()
        elif event == 'OK':
            break
    yeet.close()
    return values


def second_panel(files):
    text_columns = []
    for name, file_path in files.items():
        text_columns.append([sg.Text(name),
                             sg.Listbox(values=BANK_NAMES, select_mode='extended', key=f"{name}", size=(15, 10))])
    layout = [
        [sg.Column(text_columns, size=(700, 300), scrollable=True, key="Column")],
        [sg.OK(), sg.Cancel()],
    ]
    yeet = sg.Window('Выберите файл или папку для обработки', layout, finalize=True, background_color='#007bfb')
    event, new_values = yeet.read()
    yeet.close()
    return (event, new_values)

def error_panel(error_desc):
    event = sg.popup(f'Возникла {error_desc}', 'Вы хотите повторить ввод данных?', title='Ошибка',
                     custom_text = ('Да', 'Нет'), background_color='#007bfb' )
    if event == 'Да':
        return True
    else:
        sys.exit()

def check_query_panel(query_dict, bank_name = '', filename = ''):
    fields = []
    if bank_name=='СБЕР':
        for key, value in query_dict.items():
            fields.append([sg.Text(key, size=(60, 7), tooltip=key, background_color='#007bfb'),
                           sg.InputText(default_text=value[0], key=f'{key}_query', size=(7,5),
                                                                    background_color='white', justification='center', text_color='black'),
                           sg.InputText(default_text=value[1], key=f'{key}_house', size=(7,5),
                                         background_color='white', justification='center', text_color='black')])
        layout = [
            [sg.Text(f'Текущий файл \n{filename}', size=(70, 5), background_color='#007bfb')],
            [sg.Text('Объект строительства',size=(60, 2), background_color='#007bfb'),
             sg.Text('Очередь', size=(7, 2)), sg.Text('Дом', size=(7, 2),background_color='#007bfb')],
            [sg.Column(fields, size=(700, 700), scrollable=True, key="Column", background_color='#007bfb')],
            [sg.OK(), sg.Cancel()]
        ]
    elif bank_name!='ОСВ':
        for key, value in query_dict.items():
            fields.append([sg.Text(value[0], size=(15, 2), background_color='#007bfb'),
                           sg.Text(value[1], size=(15, 2), background_color='#007bfb'),
                           sg.InputText(default_text=value[0], key=f'{key}_query', size=(15, 2),
                                        background_color='white', justification='center', text_color='black'),
                           sg.InputText(default_text=value[1], key=f'{key}_house', size=(15, 2),
                                        background_color='white', justification='center', text_color='black')])
        layout = [[sg.Text(f'Текущий файл \n{filename}', size=(70, 5), background_color='#007bfb')],
                  [sg.Text('Текущая очередь', size=(15, 2), background_color='#007bfb'),
                   sg.Text('Текущий дом', size=(15, 2), background_color='#007bfb'),
                   sg.Text('Новая очередь', size=(15, 2),background_color='#007bfb'),
                   sg.Text('Новый дом', size=(15, 2), background_color='#007bfb')],
                  [sg.Column(fields, size=(600, 400), scrollable=True, key="Column", background_color='#007bfb', )],
                  [sg.OK(), sg.Cancel()]
                  ]
    else:
        for key, value in query_dict.items():
            fields.append([sg.Text(key, size=(60, 7), tooltip=key, background_color='#007bfb'),
                           sg.InputText(default_text=value[0], key=f'{key}_query', size=(7, 5),
                                        background_color='white', justification='center', text_color='black'),
                           sg.InputText(default_text=value[1], key=f'{key}_house', size=(7, 5),
                                        background_color='white', justification='center', text_color='black')])
        layout = [
            [sg.Text('Группа', size=(60, 2), background_color='#007bfb'),
             sg.Text('Очередь', size=(7, 2),background_color='#007bfb'), sg.Text('Дом', size=(7, 2))],
            [sg.Column(fields, size=(700, 400), scrollable=True, key="Column", background_color='#007bfb')],
            [sg.OK(), sg.Cancel()]
        ]
    yeet = sg.Window(f'Проверьте распределение очередей и домов для файла {bank_name}', layout, finalize=True, background_color='#007bfb')
    event, new_values = yeet.read()
    yeet.close()
    if event == 'Cancel':
        sys.exit()
    result = dict()
    for key, value in new_values.items():
        new_key = key[:key.rfind('_')]
        result.setdefault(new_key, []).append(value)
    return result

def check_user_values(user_data):
    if user_data['bank_file'] == '' and user_data['bank_folder'] == '':
        return 'ошибка: Не выбран файл с банковоской ведомостью'
    elif user_data['account'] == '':
        return 'ошибка: Не вывбран файл с ОСВ'
    elif user_data['bank_name'] == '' and user_data['bank_file'] != '':
        return 'ошибка: Не указан тип банка'
    else:
        return True

def end_panel(path):
    # event = sg.popup_auto_close(f'Сверка завершена', title='Завершение работы',
    #                             background_color='#007bfb', auto_close_duration = 5)
    # if event == 'OK':
    #     sys.exit()
    path = f'{path}/Сверка.xlsx'
    event = sg.popup('Сверка завершена\nОткрыть созданный файл?', background_color='#007bfb',
                         button_color=('white', '#007bfb'),
                         title='Завершение работы', custom_text=('Да', 'Нет'))
    if event == 'Да':
        Excel = win32com.client.Dispatch("Excel.Application")
        Excel.Visible = True
        Excel.Workbooks.Open(Filename = path)
        time.sleep(5)
        del Excel
    else:
        sys.exit()

