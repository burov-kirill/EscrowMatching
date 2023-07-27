import os
import sys
import time
from glob import glob
import win32com.client
import io
import PySimpleGUI as sg
from PIL import Image

from settings.update.updates import check_version, call_updater
from settings.update.config import VERSION

sg.LOOK_AND_FEEL_TABLE['SamoletTheme'] = {
                                        'BACKGROUND': '#007bfb',
                                        'TEXT': '#FFFFFF',
                                        'INPUT': '#FFFFFF',
                                        'TEXT_INPUT': '#000000',
                                        'SCROLL': '#FFFFFF',
                                        'BUTTON': ('#FFFFFF', '#007bfb'),
                                        'PROGRESS': ('#354d73', '#FFFFFF'),
                                        'BORDER': 1, 'SLIDER_DEPTH': 0,
                                        'PROGRESS_DEPTH': 0, }

# def resource_path(relative_path):
#     try:
#         base_path = sys._MEIPASS
#     except Exception:
#         base_path = os.path.abspath("")
#
#     return os.path.join(base_path, relative_path)
#
# image_path = resource_path("samolet.png")


BANK_NAMES = ['СБЕР', 'Альфа Банк', 'Совкомбанк', 'Дом РФ', 'МКБ', 'ВТБ', 'ГПБ', 'ПСБ', "ВБРР", "Промсвязьбанк"]
def set_img_option(img_path):
    img = Image.open(img_path)
    img_resized = img.resize((400, 100))
    img_byte_arr = io.BytesIO()
    img_resized.save(img_byte_arr, format='png', subsampling=0, quality=100)
    img_byte_arr = img_byte_arr.getvalue()
    return img_byte_arr

def user_action(img_path):
    values = first_panel(img_path)
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
                if event=='Выход':
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



def first_panel(img_path):
    sg.theme('SamoletTheme')
    img_byte_arr = set_img_option(img_path)
    SELECT_FRAME = [
        [sg.Listbox(values=BANK_NAMES, select_mode='LISTBOX_SELECT_MODE_SINGLE', key='bank_name', size=(30, 8)),
         sg.Column([
             [sg.pin(sg.Button('Проверка \nобновления', key='check_upd', visible=True, size=(10, 5), button_color='#1E90FF')),
              sg.pin(sg.Button('Обновить', key='upd_btn', size=(10, 5), visible=False, button_color='#0000FF'))]
               ], background_color='#007bfb')
    ]
    ]
    DOC_FRAME = [
        [sg.Checkbox('Ведомости от одного банка', default=True, key='single',
                  background_color='#007bfb')],
        [sg.Text('Выбрать файл данных банка', background_color='#007bfb')],
        [sg.Input(key='bank_file'), sg.FileBrowse(button_color='#007bfb', button_text='Выбрать')],
        [sg.Text('Выбрать папку с данными банка', background_color='#007bfb')],
        [sg.Input(key='bank_folder'), sg.FolderBrowse(button_color='#007bfb', button_text='Выбрать')],
        [sg.Text('Выбрать файл с ОСВ', background_color='#007bfb')],
        [sg.Input(key='account'), sg.FileBrowse(button_color='#007bfb', button_text='Выбрать')],
        [sg.Text('Папка для сохранения файла', background_color='#007bfb')],
        [sg.Input(key='save_to'), sg.FolderBrowse(button_color='#007bfb', button_text='Выбрать')]
    ]
    REVIEW_FRAME = [

        [sg.Checkbox('Включить функцию редактирования очередь/дом для Банка', key='check', default=True,
                     background_color='#007bfb')],
        [sg.Checkbox('Включить функцию редактирования очередь/дом для ОСВ', key='check_account', default=False,
                     background_color='#007bfb')],
        [sg.Checkbox('Редакция ОСВ по номенклатуре', key='check_nomenclature', default=True,
                     background_color='#007bfb')]
    ]

    layout = [
            [sg.Image(source=img_byte_arr)],
            [sg.Frame(layout=SELECT_FRAME, title='Выбор банка',background_color='#007bfb', size=(400, 150))],
            [sg.Frame(layout=DOC_FRAME, title='Выбор файлов', background_color='#007bfb', size=(400, 300))],
            [sg.Frame(layout=REVIEW_FRAME, title='Параметры для ревью', background_color='#007bfb', size=(400, 120))],
            [sg.OK(button_color='#007bfb', button_text='Далее'), sg.Cancel(button_color='#007bfb', button_text='Выход')]
    ]
    yeet = sg.Window(f'Сверка Банка и ОСВ {VERSION}', background_color='#007bfb', layout=layout)
    check, upd_check = False, True
    # yeet = sg.Window(f'Сверка Банка и ОСВ ver {VERSION}', background_color='#007bfb').Layout(
    #     [
    #         [sg.Image(source = img_byte_arr)],
    #         [sg.Text('Выберите тип банка', pad=(3,3), background_color='#007bfb'),
    #          sg.Listbox(values=BANK_NAMES, select_mode = 'LISTBOX_SELECT_MODE_SINGLE', key='bank_name', size=(30, 8))],
    #         [sg.Text('Доступно обновление',visible=False, key='upd_txt'), sg.Button('Обновить', visible=False, key='upd_btn')],
    #         [sg.Button('Пакет', visible=False, key='pocket'), sg.Button('Файл', visible=False, key='file')],
    #         [sg.Text('Выбрать файл данных банка', background_color='#007bfb')],
    #         [sg.Input(key='bank_file'), sg.FileBrowse()],
    #         [sg.Text('Выбрать папку с данными банка', background_color='#007bfb')],
    #         [sg.Input(key='bank_folder'), sg.FolderBrowse()],
    #         [sg.Text('Выбрать файл с ОСВ', background_color='#007bfb')],
    #         [sg.Input(key='account'), sg.FileBrowse()],
    #         [sg.Text('Папка для сохранения файла', background_color='#007bfb')],
    #         [sg.Input(key='save_to'), sg.FolderBrowse()],
    #         [sg.Text('Настройка параметров обработки', pad=(3, 3), auto_size_text=True,
    #                  relief='solid', background_color='#007bfb')],
    #         [sg.Radio('Банковские ведомости от одного банка', "RADIO1", default=True, key='single', background_color='#007bfb')],
    #         [sg.Radio('Банковские ведомости от разных банков', "RADIO1", default=False, background_color='#007bfb')],
    #         [sg.Text('Настройка параметров для ревью', justification='center',
    #                  relief = 'solid', background_color='#007bfb')],
    #         [sg.Checkbox('Включить функцию редактирования очередь/дом для Банка', key='check', default=True, tooltip=tooltip_bank, background_color='#007bfb')],
    #         [sg.Checkbox('Включить функцию редактирования очередь/дом для ОСВ', key='check_account', default=False, tooltip=tooltip_account, background_color='#007bfb')],
    #         [sg.Checkbox('Редакция ОСВ по номенклатуре', key='check_nomenclature', default=True, tooltip=tooltip_redaction, background_color='#007bfb')],
    #
    #         [sg.OK(), sg.Cancel()]
    #     ])
    # upd_check = check_version()
    # if not upd_check:
    #     yeet['upd_txt'].Update(visible=True)
    #     yeet['upd_btn'].Update(visible=True)
    while True:
        event, values = yeet.Read(timeout=10)
        if check:
            upd_check = check_version()
            check = False
        if event in ('Выход', sg.WIN_CLOSED):
            sys.exit()
        if event == 'check_upd':
            check = True
        if not upd_check:
            # yeet['upd_txt'].Update(visible=True)
            yeet['upd_btn'].Update(visible=True)
            yeet['check_upd'].Update(visible=False)
        if event == 'upd_btn':
            yeet.close()
            call_updater('pocket')
        elif event == 'Далее':
            break
        # if not upd_check:
        #     yeet['upd_txt'].Update(visible=True)
        #     yeet['upd_btn'].Update(visible=True)
        # if event == 'upd_btn':
        #     yeet['pocket'].Update(visible=True)
        #     yeet['file'].Update(visible=True)
        # if event in ('pocket', 'file'):
        #     yeet.close()
        #     call_updater(event)
    yeet.close()
    return values


def second_panel(files):
    text_columns = []
    for name, file_path in files.items():
        text_columns.append([sg.Text(name, background_color='#007bfb'), sg.Push(),
                             sg.Listbox(values=BANK_NAMES, select_mode='LISTBOX_SELECT_MODE_SINGLE',
                                        key=f"{name}", size=(15, 10))])
    layout = [
        [sg.Frame(title = 'Распределение файлов по банкам',
                  layout = [[sg.Column(text_columns, scrollable=True, key="Column", background_color='#007bfb')]],
                  size=(700, 300), background_color='#007bfb')],
        [sg.OK(button_color='#007bfb', button_text='Далее'), sg.Cancel(button_color='#007bfb', button_text='Выход')]
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

def get_filename(path):
    return path[path.rfind('/')+1:]

def check_query_panel(query_dict, bank_name = '', filename = ''):
    fields = []
    # col1, col2, col3 = [[sg.Text('Объект строительства', size=(7, 2), background_color='#007bfb')]],\
    #     [[sg.Text('Очередь', size=(7, 2), background_color='#007bfb')]], [[sg.Text('Дом', size=(7, 2),background_color='#007bfb')]]
    if bank_name=='СБЕР':
        for key, value in query_dict.items():
            height = len(key)//60+1
            fields.append([sg.Col([[sg.Text(key,size=(60, height), background_color='#007bfb'),
                                    sg.InputText(default_text=value[0], size=(10, height), key=f'{key}_query',
                                                 background_color='white', justification='center', text_color='black'),
                                    sg.InputText(default_text=value[1], size=(10, height), key=f'{key}_house',
                                                 background_color='white', justification='center', text_color='black')
                                    ]])])
            # col1.append([sg.Text(key,size=(60, 7), tooltip=key, background_color='#007bfb')])
            # col2.append([sg.InputText(default_text=value[0],size=(60, 7),key=f'{key}_query',
            #                         background_color='white', justification='center', text_color='black')])
            # col3.append([sg.InputText(default_text=value[1], size=(60, 7), key=f'{key}_house',
            #                         background_color='white', justification='center', text_color='black')])
            # fields.append([sg.Text(key, size=(60, 7), tooltip=key, background_color='#007bfb'),
            #                sg.InputText(default_text=value[0], key=f'{key}_query', size=(7,5),
            #                                                         background_color='white', justification='center', text_color='black'),
            #                sg.InputText(default_text=value[1], key=f'{key}_house', size=(7,5),
            #                              background_color='white', justification='center', text_color='black')])
        # layout = [
        #     [sg.Text(f'Текущий файл \n{filename}', size=(70, 5), background_color='#007bfb')],
        #     [sg.Text('Объект строительства',size=(60, 2), background_color='#007bfb'),
        #      sg.Text('Очередь', size=(7, 2)), sg.Text('Дом', size=(7, 2),background_color='#007bfb')],
        #     [sg.Column(fields, size=(700, 700), scrollable=True, key="Column", background_color='#007bfb')],
        #     [sg.OK(), sg.Cancel()]
        # ]
        # FRAME = [
        #     [sg.Column([[sg.Column(col1, vertical_alignment='top', size=(200,200)), sg.Column(col2, size=(200,200), vertical_alignment='top'),
        #            sg.Column(col3, size=(200,200), vertical_alignment='top')]], scrollable = True,
        #                background_color='#007bfb',vertical_scroll_only = False)]
        # ]
        FRAME = [
            [sg.Column(fields,size=(700, 600), scrollable = True, background_color='#007bfb')]
        ]
        layout = [[sg.Text(f'Текущий файл \n{get_filename(filename)}', background_color='#007bfb', font='bold')],
                  [sg.Frame(title='Корректировка номенклатурных групп', layout = FRAME, background_color='#007bfb', size=(700, 600))],
                    # [sg.Frame(title='Корректировка номенклатурных групп', layout=[col1])],
                  [sg.OK(button_color='#007bfb', button_text='Далее'), sg.Cancel(button_color='#007bfb', button_text='Выход')]]

    elif bank_name!='ОСВ':
        for key, value in query_dict.items():
            fields.append([sg.Col([[sg.Text(value[0], size=(15, 2), background_color='#007bfb'),
                                    sg.Text(value[1], size=(15, 2), background_color='#007bfb'),
                                    sg.InputText(default_text=value[0], key=f'{key}_query', size=(15, 2),
                                                 background_color='white', justification='center', text_color='black'),
                                    sg.InputText(default_text=value[1], key=f'{key}_house', size=(15, 2),
                                                 background_color='white', justification='center', text_color='black')
                                    ]])])
            # fields.append([sg.Text(value[0], size=(15, 2), background_color='#007bfb'),
            #                sg.Text(value[1], size=(15, 2), background_color='#007bfb'),
            #                sg.InputText(default_text=value[0], key=f'{key}_query', size=(15, 2),
            #                             background_color='white', justification='center', text_color='black'),
            #                sg.InputText(default_text=value[1], key=f'{key}_house', size=(15, 2),
            #                             background_color='white', justification='center', text_color='black')])
        FRAME = [
            [sg.Column(fields, size=(700, 600), scrollable=True, background_color='#007bfb')]
        ]
        layout = [
                  [sg.Text(f'Текущий файл \n{get_filename(filename)}', font='bold', background_color='#007bfb')],
                  [sg.Frame(title='Корректировка номенклатурных групп', layout=FRAME, background_color='#007bfb',
                            size=(700, 600))],
                  # [sg.Column(fields, size=(600, 400), scrollable=True, key="Column", background_color='#007bfb', )],
                  [sg.OK(button_color='#007bfb', button_text='Далее'), sg.Cancel(button_color='#007bfb', button_text='Выход')]
                  ]
    else:
        for key, value in query_dict.items():
            height = len(key) // 60 + 1
            fields.append([sg.Col([[sg.Text(key, size=(60, height), tooltip=key, background_color='#007bfb'),
                                    sg.InputText(default_text=value[0], key=f'{key}_query', size=(7, height),
                                                 background_color='white', justification='center', text_color='black'),
                                    sg.InputText(default_text=value[1], key=f'{key}_house', size=(7, height),
                                                 background_color='white', justification='center', text_color='black')
                                    ]], background_color='#007bfb')])
            # fields.append([sg.Text(key, size=(60, 7), tooltip=key, background_color='#007bfb'),
            #                sg.InputText(default_text=value[0], key=f'{key}_query', size=(7, 5),
            #                             background_color='white', justification='center', text_color='black'),
            #                sg.InputText(default_text=value[1], key=f'{key}_house', size=(7, 5),
            #                             background_color='white', justification='center', text_color='black')])
        FRAME = [
            [sg.Column(fields, size=(700, 600), scrollable=True, background_color='#007bfb')]
        ]
        layout = [
            # [sg.Text(f'Текущий файл \n{get_filename(filename)}', font='bold', background_color='#007bfb')],
            [sg.Frame(title='Корректировка номенклатурных групп', layout=FRAME, background_color='#007bfb',
                      size=(700, 600))],
            # [sg.Column(fields, size=(700, 400), scrollable=True, key="Column", background_color='#007bfb')],
            [sg.OK(button_color='#007bfb', button_text='Далее'), sg.Cancel(button_color='#007bfb', button_text='Выход')]
        ]
    yeet = sg.Window(f'Проверьте распределение очередей и домов для файла {bank_name}',  layout, finalize=True,
                     background_color='#007bfb')
    while True:
        event, new_values = yeet.read()
        if event in ('Выход', sg.WIN_CLOSED):
            sys.exit()
        elif event == 'Далее':
            break
    yeet.close()
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

