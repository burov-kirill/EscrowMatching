import unittest

from classes.account import AccountFile
from classes.bank import BankFile


class TestCalc(unittest.TestCase):

    account_file_dict = \
        {
            'Алхимово': {
                'account': r"C:\Users\cyril\Desktop\Самолет\Алхимово\ОСВ по счету 009.СЭ за ... - 1 квартал 2023 г.АЛХИМОВО.xlsx",
                'bank_name': ['СБЕР'],
                'type': False,
                'check_nomenclature': True,
                'check_account': False
            },
            'Томилино': {
                'account': r"C:\Users\cyril\Desktop\Самолет\Томилино\ОСВ по счету 009.СЭ за ... - 2022 г. ООО  СЗ  САМОЛЕТ-ТОМИЛИНО.xlsx",
                'bank_name': ['Остафьево Банк'],
                'type': False,
                'check_nomenclature': True,
                'check_account': False
            },
            'Некрасовка': {
                'account': r"C:\Users\cyril\Desktop\Самолет\Некрасовка\ОСВ по счету 009.СЭ за ... - 2022 г. ООО  СЗ  НЕКРАСОВКА-ИНВЕСТ.xlsx",
                'bank_name': ['МКБ'],
                'type': False,
                'check_nomenclature': True,
                'check_account': False
            },
            'Верейская': {
                'account': r"C:\Users\cyril\Desktop\Самолет\Верейская\ОСВ по счету 009.СЭ за ... - 2022 г. АО  СЗ  САМОЛЕТ-ВЕРЕЙСКАЯ.xlsx",
                'bank_name': ['СБЕР'],
                'type': False,
                'check_nomenclature': True,
                'check_account': False
            },
            'Горки Парк': {
                'account': r"C:\Users\cyril\Desktop\Самолет\Горки Парк\ОСВ 009.СЭ за ... - 2022 г. ООО  СЗ  САМОЛЕТ-КОРОБОВО.xlsx",
                'bank_name': ['СБЕР'],
                'type': False,
                'check_nomenclature': True,
                'check_account': False
            },
            'Егорово Парк': {
                'account': r"C:\Users\cyril\Desktop\Самолет\Егорово Парк, Сам-Жилино (Предварительный анализ)\ОСВ по счету 009.СЭ за ... - 2022 г. ООО  СЗ  САМОЛЕТ-ЖИЛИНО.xlsx",
                'bank_name': ['СБЕР'],
                'type': False,
                'check_nomenclature': True,
                'check_account': False
            },
            'Заречье': {
                'account': r"C:\Users\cyril\Desktop\Самолет\Заречье\ОСВ по счету 009.СЭ за ... - 2022 г. ООО  СЗ  САМОЛЕТ-ЗАРЕЧЬЕ.xlsx",
                'bank_name': ['Совкомбанк'],
                'type': False,
                'check_nomenclature': True,
                'check_account': False
            },
            'Иванкино': {
                'account': r"C:\Users\cyril\Desktop\Самолет\Иванкино\Оборотно-сальдовая ведомость по счету 009.СЭ за ... - 2022 г. ООО  СЗ  САМОЛЕТ-ОЛИМП.xlsx",
                'bank_name': ['МКБ'],
                'type': False,
                'check_nomenclature': True,
                'check_account': False
            },
            'Лайково': {
                'account': r"C:\Users\cyril\Desktop\Самолет\Лайково\Оборотно-сальдовая ведомость по счету 009.СЭ за ... - 2022 г. ООО  СЗ  САМОЛЕТ-ЛАЙКОВО.xlsx",
                'bank_name': ['Дом РФ'],
                'type': False,
                'check_nomenclature': True,
                'check_account': False
            },
            'Люберцы': {
                'account': r"C:\Users\cyril\Desktop\Самолет\Люберцы\Оборотно-сальдовая ведомость по счету 009.СЭ за ... - 2022 г. ООО  СЗ  САМОЛЕТ ДЕВЕЛОПМЕНТ.xlsx",
                'bank_name': ['Альфа Банк'],
                'type': False,
                'check_nomenclature': True,
                'check_account': False
            },
            'Молжаниново': {
                'account': r"C:\Users\cyril\Desktop\Самолет\Молжаниново\ОСВ по счету 009.СЭ за ... - 2022 г. ООО  СЗ  САМОЛЕТ-МОЛЖАНИНОВО.xlsx",
                'bank_name': ['МКБ'],
                'type': False,
                'check_nomenclature': True,
                'check_account': False
            },
            'Мытищи': {
                'account': r"C:\Users\cyril\Desktop\Самолет\Мытищи Парк (Самолет-Мытищи)\ОСВ по счету 009.СЭ за ... - 2022 г. ООО  СЗ  САМОЛЕТ-МЫТИЩИ.xlsx",
                'bank_name': ['Альфа Банк'],
                'type': False,
                'check_nomenclature': True,
                'check_account': False
            },
            'Новоданиловская': {
                'account': r"C:\Users\cyril\Desktop\Самолет\Новоданиловская 8\ОСВ по счету 009.СЭ за ... - 2022 г. ООО  СЗ  ДМ АПАРТМЕНТС.xlsx",
                'bank_name': ['Дом РФ'],
                'type': False,
                'check_nomenclature': True,
                'check_account': False
            },
            'Остафьево': {
                'account': r"C:\Users\cyril\Desktop\Самолет\Остафьево (СР-Групп)\Оборотно-сальдовая ведомость по счету 009.СЭ за ... - 2022 г. ООО  СЗ  СР-ГРУПП.xlsx",
                'bank_name': ['ВТБ'],
                'type': False,
                'check_nomenclature': True,
                'check_account': False
            },
            'Путилково': {
                'account': r"C:\Users\cyril\Desktop\Самолет\Путилково\ОСВ по счету 009.СЭ за ... - 2022 г. ООО  СЗ  САМОЛЕТ-ПУТИЛКОВО.xlsx",
                'bank_name': ['ГПБ'],
                'type': False,
                'check_nomenclature': True,
                'check_account': False
            },
            'Новое Внуково': {
                'account': r"C:\Users\cyril\Desktop\Самолет\Новое Внуково\ОСВ Санино.xlsx",
                'bank_name': ['СБЕР'],
                'type': False,
                'check_nomenclature': True,
                'check_account': False
            },
            'Прибрежный парк': {
                'account': r"C:\Users\cyril\Desktop\Самолет\Парк\ОСВ Прибрежный парк.xlsx",
                'bank_name': ['СБЕР'],
                'type': False,
                'check_nomenclature': True,
                'check_account': False
            },
            'Пригород Лесное': {
                'account': r"C:\Users\cyril\Desktop\Самолет\Пригород\ОСВ по счету 009.СЭ за ... - 2022 г. ООО  СЗ  ПРИГОРОД ЛЕСНОЕ.xlsx",
                'bank_name': ['СБЕР'],
                'type': False,
                'check_nomenclature': True,
                'check_account': False
            },
            'Пятницкие кварталы': {
                'account': r"C:\Users\cyril\Desktop\Самолет\Пятницкие кварталы\ОСВ по счету 009.СЭ за ... - 2022 г. ООО  СЗ  САМОЛЕТ-ЮРЛОВО.xlsx",
                'bank_name': ['СБЕР'],
                'type': False,
                'check_nomenclature': True,
                'check_account': False
            },
            'Спутник': {
                'account': r"C:\Users\cyril\Desktop\Самолет\Спутник\Оборотно-сальдовая ведомость по счету 009.СЭ за ... - 2022 г. ООО  СЗ  БУХТА ЛЭНД.xlsx",
                'bank_name': ['ПСБ'],
                'type': False,
                'check_nomenclature': True,
                'check_account': False
            },
            'Тропарево Парк': {
                'account': r"C:\Users\cyril\Desktop\Самолет\Тропарево\ОСВ по счету 009.СЭ за ... - 2022 г. ООО  СЗ  САМОЛЕТ-ДУДКИНО.xlsx",
                'bank_name': ['СБЕР'],
                'type': False,
                'check_nomenclature': True,
                'check_account': False
            }
        }

    control_account_sum_dict = {'Алхимово': 8674530750, 'Верейская': 3007479604.49, 'Горки Парк': 12059017028.80,
                        'Долина Яузы': 336466065.72,
                        'Егорово Парк': 6671997131.40, 'Заречье': 6796629905.21, 'Иванкино': 132667226.56,
                        'Лайково': 431609856.51,
                        'Люберцы': 23157415074.02, 'Молжаниново': 9983314727.20, 'Мытищи': 23785546445.83,
                        'Новоданиловская': 7498683812.03,
                        'Остафьево': 869364295.78, 'Путилково': 10052991966.76, 'Новое Внуково': 18734637421.29,
                        'Прибрежный парк': 16330258011.93,
                        'Пригород Лесное': 28919689630.58, 'Пятницкие кварталы': 4616973869.59,
                        'Спутник': 12722996123.14, 'Тропарево Парк': 9053913732.78,
                        'Некрасовка': 6884758292.17, 'Томилино': 17134969664.61}



    bank_file_dict = {
        'Алхимово': {
            'bank_file': r"C:\Users\cyril\Desktop\Самолет\Алхимово\Алхимово общий отчет-01.03.2023-31.03.2023.xlsx",
            'bank_folder': '',
            'bank_name': ['СБЕР'],
            'single': True,
            'file_to_bank': dict(),
            'check': False
        },
        # 'Некрасовка': {
        #     'bank_file': r"C:\Users\cyril\Desktop\Самолет\Некрасовка\Банк.xlsx",
        #     'bank_folder': '',
        #     'bank_name': ['МКБ'],
        #     'single': True,
        #     'file_to_bank': dict(),
        #     'check': False
        # },
        'Томилино': {
            'bank_file': r"C:\Users\cyril\Desktop\Самолет\Томилино\Банк.xlsx",
            'bank_folder': '',
            'bank_name': ['ВТБ'],
            'single': True,
            'file_to_bank': dict(),
            'check': False
        },
        'Верейская': {
            'bank_file': '',
            'bank_folder': r'C:\Users\cyril\Desktop\Самолет\Верейская\Выписки',
            'bank_name': ['СБЕР'],
            'single': True,
            'file_to_bank': {
                'ЖК «Горки Парк» корп_EscrowReport7_01.12.2022-31.12.2022 1.1.xlsx': (
                    'C:/Users/cyril/Desktop/Самолет/Верейская/Выписки\\ЖК «Горки Парк» корп_EscrowReport7_01.12.2022-31.12.2022 1.1.xlsx',
                    'СБЕР'),
                'ЖК «Горки Парк» корп_EscrowReport8_01.12.2022-31.12.2022 1.2.xlsx': (
                    'C:/Users/cyril/Desktop/Самолет/Верейская/Выписки\\ЖК «Горки Парк» корп_EscrowReport8_01.12.2022-31.12.2022 1.2.xlsx',
                    'СБЕР'),
                'ЖК «Горки Парк» корп_EscrowReport9_01.12.2022-31.12.2022 1.3.xlsx': (
                    'C:/Users/cyril/Desktop/Самолет/Верейская/Выписки\\ЖК «Горки Парк» корп_EscrowReport9_01.12.2022-31.12.2022 1.3.xlsx',
                    'СБЕР'),
                'ЖК Горки Парк  1-ый _EscrowReport3_01.12.2022-31.12.2022 3.1.xlsx': (
                    'C:/Users/cyril/Desktop/Самолет/Верейская/Выписки\\ЖК Горки Парк  1-ый _EscrowReport3_01.12.2022-31.12.2022 3.1.xlsx',
                    'СБЕР'),
                'ЖК Горки Парк  1-ый _EscrowReport4_01.12.2022-31.12.2022 3.2.xlsx': (
                    'C:/Users/cyril/Desktop/Самолет/Верейская/Выписки\\ЖК Горки Парк  1-ый _EscrowReport4_01.12.2022-31.12.2022 3.2.xlsx',
                    'СБЕР'),
                'ЖК Горки Парк Жилой _EscrowReport1_01.12.2022-31.12.2022 4.1.xlsx': (
                    'C:/Users/cyril/Desktop/Самолет/Верейская/Выписки\\ЖК Горки Парк Жилой _EscrowReport1_01.12.2022-31.12.2022 4.1.xlsx',
                    'СБЕР'),
                'ЖК Горки Парк Жилой _EscrowReport2_01.12.2022-31.12.2022 4.2.xlsx': (
                    'C:/Users/cyril/Desktop/Самолет/Верейская/Выписки\\ЖК Горки Парк Жилой _EscrowReport2_01.12.2022-31.12.2022 4.2.xlsx',
                    'СБЕР'),
                'ЖК Горки Парк корпус_EscrowReport10_01.12.2022-31.12.2022 2.1.xlsx': (
                    'C:/Users/cyril/Desktop/Самолет/Верейская/Выписки\\ЖК Горки Парк корпус_EscrowReport10_01.12.2022-31.12.2022 2.1.xlsx',
                    'СБЕР'),
                'ЖК Горки Парк корпус_EscrowReport11_01.12.2022-31.12.2022 2.2.xlsx': (
                    'C:/Users/cyril/Desktop/Самолет/Верейская/Выписки\\ЖК Горки Парк корпус_EscrowReport11_01.12.2022-31.12.2022 2.2.xlsx',
                    'СБЕР'),
                'ЖК Горки Парк корпус_EscrowReport12_01.12.2022-31.12.2022 5.1.xlsx': (
                    'C:/Users/cyril/Desktop/Самолет/Верейская/Выписки\\ЖК Горки Парк корпус_EscrowReport12_01.12.2022-31.12.2022 5.1.xlsx',
                    'СБЕР'),
                'ЖК Горки Парк корпус_EscrowReport13_01.12.2022-31.12.2022 5.2.xlsx': (
                    'C:/Users/cyril/Desktop/Самолет/Верейская/Выписки\\ЖК Горки Парк корпус_EscrowReport13_01.12.2022-31.12.2022 5.2.xlsx',
                    'СБЕР'),
                'ЖК Горки Парк корпус_EscrowReport5_01.12.2022-31.12.2022 7.1.xlsx': (
                    'C:/Users/cyril/Desktop/Самолет/Верейская/Выписки\\ЖК Горки Парк корпус_EscrowReport5_01.12.2022-31.12.2022 7.1.xlsx',
                    'СБЕР'),
                'ЖК Горки Парк корпус_EscrowReport6_01.12.2022-31.12.2022 7.2.xlsx': (
                    'C:/Users/cyril/Desktop/Самолет/Верейская/Выписки\\ЖК Горки Парк корпус_EscrowReport6_01.12.2022-31.12.2022 7.2.xlsx',
                    'СБЕР')
            },
            'check': False
        },
        'Горки Парк': {
            'bank_file': '',
            'bank_folder': r'C:\Users\cyril\Desktop\Самолет\Горки Парк\Выписки банка',
            'bank_name': ['СБЕР'],
            'single': True,
            'file_to_bank': {
                '1.1.xlsx': (
                    'C:/Users/cyril/Desktop/Самолет/Горки Парк/Выписки банка\\1.1.xlsx',
                    'СБЕР'),
                '1.2.xlsx': (
                    'C:/Users/cyril/Desktop/Самолет/Горки Парк/Выписки банка\\1.2.xlsx',
                    'СБЕР'),
                '1.3.xlsx': (
                    'C:/Users/cyril/Desktop/Самолет/Горки Парк/Выписки банка\\1.3.xlsx',
                    'СБЕР'),
                '3.1.xlsx': (
                    'C:/Users/cyril/Desktop/Самолет/Горки Парк/Выписки банка\\3.1.xlsx',
                    'СБЕР'),
                'ЖК Горки Парк  1-ый _EscrowReport4_01.12.2022-31.12.2022 3.2.xlsx': (
                    'C:/Users/cyril/Desktop/Самолет/Горки Парк/Выписки банка\\ЖК Горки Парк  1-ый _EscrowReport4_01.12.2022-31.12.2022 3.2.xlsx',
                    'СБЕР'),
                'ЖК Горки Парк Жилой _EscrowReport1_01.12.2022-31.12.2022 4.1.xlsx': (
                    'C:/Users/cyril/Desktop/Самолет/Горки Парк/Выписки банка\\ЖК Горки Парк Жилой _EscrowReport1_01.12.2022-31.12.2022 4.1.xlsx',
                    'СБЕР'),
                'ЖК Горки Парк Жилой _EscrowReport2_01.12.2022-31.12.2022 4.2.xlsx': (
                    'C:/Users/cyril/Desktop/Самолет/Горки Парк/Выписки банка\\ЖК Горки Парк Жилой _EscrowReport2_01.12.2022-31.12.2022 4.2.xlsx',
                    'СБЕР'),
                'ЖК Горки Парк корпус_EscrowReport10_01.12.2022-31.12.2022 2.1.xlsx': (
                    'C:/Users/cyril/Desktop/Самолет/Горки Парк/Выписки банка\\ЖК Горки Парк корпус_EscrowReport10_01.12.2022-31.12.2022 2.1.xlsx',
                    'СБЕР'),
                'ЖК Горки Парк корпус_EscrowReport11_01.12.2022-31.12.2022 2.2.xlsx': (
                    'C:/Users/cyril/Desktop/Самолет/Горки Парк/Выписки банка\\ЖК Горки Парк корпус_EscrowReport11_01.12.2022-31.12.2022 2.2.xlsx',
                    'СБЕР'),
                'ЖК Горки Парк корпус_EscrowReport12_01.12.2022-31.12.2022 5.1.xlsx': (
                    'C:/Users/cyril/Desktop/Самолет/Горки Парк/Выписки банка\\ЖК Горки Парк корпус_EscrowReport12_01.12.2022-31.12.2022 5.1.xlsx',
                    'СБЕР'),
                'ЖК Горки Парк корпус_EscrowReport13_01.12.2022-31.12.2022 5.2.xlsx': (
                    'C:/Users/cyril/Desktop/Самолет/Горки Парк/Выписки банка\\ЖК Горки Парк корпус_EscrowReport13_01.12.2022-31.12.2022 5.2.xlsx',
                    'СБЕР'),
                'ЖК Горки Парк корпус_EscrowReport5_01.12.2022-31.12.2022 7.1.xlsx': (
                    'C:/Users/cyril/Desktop/Самолет/Горки Парк/Выписки банка\\ЖК Горки Парк корпус_EscrowReport5_01.12.2022-31.12.2022 7.1.xlsx',
                    'СБЕР'),
                'ЖК Горки Парк корпус_EscrowReport6_01.12.2022-31.12.2022 7.2.xlsx': (
                    'C:/Users/cyril/Desktop/Самолет/Горки Парк/Выписки банка\\ЖК Горки Парк корпус_EscrowReport6_01.12.2022-31.12.2022 7.2.xlsx',
                    'СБЕР')
            },
            'check': False
        },
        'Егорово Парк': {
            'bank_file': '',
            'bank_folder': r'C:\Users\cyril\Desktop\Самолет\Егорово Парк, Сам-Жилино (Предварительный анализ)\Выписки банка',
            'bank_name': ['СБЕР'],
            'single': True,
            'file_to_bank': {
                'ЖК Егорово Парк - жи_EscrowReport1_01.12.2022-08.01.2023  дом1.xlsx': (
                    'C:/Users/cyril/Desktop/Самолет/Егорово Парк, Сам-Жилино (Предварительный анализ)/Выписки банка\\ЖК Егорово Парк - жи_EscrowReport1_01.12.2022-08.01.2023  дом1.xlsx',
                    'СБЕР'),
                'ЖК Егорово Парк - жи_EscrowReport2_01.12.2022-08.01.2023  дом3.xlsx': (
                    'C:/Users/cyril/Desktop/Самолет/Егорово Парк, Сам-Жилино (Предварительный анализ)/Выписки банка\\ЖК Егорово Парк - жи_EscrowReport2_01.12.2022-08.01.2023  дом3.xlsx',
                    'СБЕР'),
                'ЖК Егорово Парк - жи_EscrowReport3_01.12.2022-08.01.2023  дом 2.xlsx': (
                    'C:/Users/cyril/Desktop/Самолет/Егорово Парк, Сам-Жилино (Предварительный анализ)/Выписки банка\\ЖК Егорово Парк - жи_EscrowReport3_01.12.2022-08.01.2023  дом 2.xlsx',
                    'СБЕР'),
                'ЖК Егорово Парк - жи_EscrowReport4_01.12.2022-08.01.2023  дом 4.xlsx': (
                    'C:/Users/cyril/Desktop/Самолет/Егорово Парк, Сам-Жилино (Предварительный анализ)/Выписки банка\\ЖК Егорово Парк - жи_EscrowReport4_01.12.2022-08.01.2023  дом 4.xlsx',
                    'СБЕР')
            },
            'check': False
        },
        'Заречье': {
            'bank_file': r"C:\Users\cyril\Desktop\Самолет\Заречье\Выписка СЗ Самолет-Заречье 01.01.2019 - 31.12.2022_накопит.xlsx",
            'bank_folder': '',
            'bank_name': ['Совкомбанк'],
            'single': True,
            'file_to_bank': dict(),
            'check': False
        },
        # 'Иванкино': {
        #     'bank_file': r"C:\Users\cyril\Desktop\Самолет\Иванкино\Выписка банка на 31.12.2022.xlsx",
        #     'bank_folder': '',
        #     'bank_name': ['МКБ'],
        #     'single': True,
        #     'file_to_bank': dict(),
        #     'check': False
        # },
        'Лайково': {
            'bank_file': r"C:\Users\cyril\Desktop\Самолет\Лайково\Счета ЭСКРОУ_1043532145_2023-01-08.xlsx",
            'bank_folder': '',
            'bank_name': ['Дом РФ'],
            'single': True,
            'file_to_bank': dict(),
            'check': False
        },
        'Люберцы': {
            'bank_file': r"C:\Users\cyril\Desktop\Самолет\Люберцы\Выписка из банка ООО СЗ САМОЛЕТ ДЕВЕЛОПМЕНТ 30.12.2022-08.01.2023.xlsx",
            'bank_folder': '',
            'bank_name': ['Альфа Банк'],
            'single': True,
            'file_to_bank': dict(),
            'check': False
        },
        # 'Молжаниново': {
        #     'bank_file': r"C:\Users\cyril\Desktop\Самолет\Молжаниново\Выписка банка 07.01.2023.xlsx",
        #     'bank_folder': '',
        #     'bank_name': ['МКБ'],
        #     'single': True,
        #     'file_to_bank': dict(),
        #     'check': False
        # },
        'Мытищи': {
            'bank_file': r"C:\Users\cyril\Desktop\Самолет\Мытищи Парк (Самолет-Мытищи)\Выписка  СЗ САМОЛЕТ-МЫТИЩИ 30.12.2022-08.01.2023.xlsx",
            'bank_folder': '',
            'bank_name': ['Альфа Банк'],
            'single': True,
            'file_to_bank': dict(),
            'check': False
        },
        'Новоданиловская': {
            'bank_file': r"C:\Users\cyril\Desktop\Самолет\Новоданиловская 8\Счета ЭСКРОУ_850474049_2022-12-31.xlsx",
            'bank_folder': '',
            'bank_name': ['Дом РФ'],
            'single': True,
            'file_to_bank': dict(),
            'check': False
        },
        'Остафьево': {
            'bank_file': r"C:\Users\cyril\Desktop\Самолет\Остафьево (СР-Групп)\CommonClientEscrowReport_2023_01_01_00_00_7731319243.xlsx",
            'bank_folder': '',
            'bank_name': ['ВТБ'],
            'single': True,
            'file_to_bank': dict(),
            'check': False
        },
        'Путилково': {
            'bank_file': r"C:\Users\cyril\Desktop\Самолет\Путилково\Путилково 31.12.22-2.xlsx",
            'bank_folder': '',
            'bank_name': ['ГПБ'],
            'single': True,
            'file_to_bank': dict(),
            'check': False
        },
        'Спутник': {
            'bank_file': '',
            'bank_folder': r'C:\Users\cyril\Desktop\Самолет\Спутник\Выписки',
            'bank_name': '',
            'single': False,
            'file_to_bank': {
                'отчет эскроу дом рф 31.12.2022.xlsx': (
                    'C:/Users/cyril/Desktop/Самолет/Спутник/Выписки\\отчет эскроу дом рф 31.12.2022.xlsx',
                    'Дом РФ'),
                'отчет эскроу совком 08.01.2023.xlsx': (
                    'C:/Users/cyril/Desktop/Самолет/Спутник/Выписки\\отчет эскроу совком 08.01.2023.xlsx',
                    'Совкомбанк'),
                'Отчет_по_счетам_Эскроу_30.09.2022 ПСБ.xlsx': (
                    'C:/Users/cyril/Desktop/Самолет/Спутник/Выписки\\Отчет_по_счетам_Эскроу_30.09.2022 ПСБ.xlsx',
                    'ПСБ')
            },
            'check': False
        },
        'Новое Внуково': {
            'bank_file': '',
            'bank_folder': r'C:\Users\cyril\Desktop\Самолет\Новое Внуково\выписки банка',
            'bank_name': ['СБЕР'],
            'single': True,
            'file_to_bank': {
                'ЖК «Новое Внуково» Н_EscrowReport10_01.12.2022-08.01.2023 д14.xlsx': (
                    'C:/Users/cyril/Desktop/Самолет/Новое Внуково/выписки банка\\ЖК «Новое Внуково» Н_EscrowReport10_01.12.2022-08.01.2023 д14.xlsx',
                    'СБЕР'),
                'ЖК «Новое Внуково» Н_EscrowReport11_01.12.2022-08.01.2023  д15.xlsx': (
                    'C:/Users/cyril/Desktop/Самолет/Новое Внуково/выписки банка\\ЖК «Новое Внуково» Н_EscrowReport11_01.12.2022-08.01.2023  д15.xlsx',
                    'СБЕР'),
                'ЖК «Новое Внуково» Н_EscrowReport12_01.12.2022-08.01.2023   д16.xlsx': (
                    'C:/Users/cyril/Desktop/Самолет/Новое Внуково/выписки банка\\ЖК «Новое Внуково» Н_EscrowReport12_01.12.2022-08.01.2023   д16.xlsx',
                    'СБЕР'),
                'ЖК «Новое Внуково» Н_EscrowReport1_01.12.2022-08.01.2023  д17.xlsx': (
                    'C:/Users/cyril/Desktop/Самолет/Новое Внуково/выписки банка\\ЖК «Новое Внуково» Н_EscrowReport1_01.12.2022-08.01.2023  д17.xlsx',
                    'СБЕР'),
                'ЖК «Новое Внуково» Н_EscrowReport2_01.12.2022-08.01.2023  д18.xlsx': (
                    'C:/Users/cyril/Desktop/Самолет/Новое Внуково/выписки банка\\ЖК «Новое Внуково» Н_EscrowReport2_01.12.2022-08.01.2023  д18.xlsx',
                    'СБЕР'),
                'ЖК «Новое Внуково» Н_EscrowReport3_01.12.2022-08.01.2023   д19.xlsx': (
                    'C:/Users/cyril/Desktop/Самолет/Новое Внуково/выписки банка\\ЖК «Новое Внуково» Н_EscrowReport3_01.12.2022-08.01.2023   д19.xlsx',
                    'СБЕР'),
                'ЖК «Новое Внуково» Н_EscrowReport4_01.12.2022-08.01.2023.xlsx': (
                    'C:/Users/cyril/Desktop/Самолет/Новое Внуково/выписки банка\\ЖК «Новое Внуково» Н_EscrowReport4_01.12.2022-08.01.2023.xlsx',
                    'СБЕР'),
                'ЖК «Новое Внуково» Н_EscrowReport5_01.12.2022-08.01.2023.xlsx': (
                    'C:/Users/cyril/Desktop/Самолет/Новое Внуково/выписки банка\\ЖК «Новое Внуково» Н_EscrowReport5_01.12.2022-08.01.2023.xlsx',
                    'СБЕР'),
                'ЖК «Новое Внуково» Н_EscrowReport6_01.12.2022-08.01.2023.xlsx': (
                    'C:/Users/cyril/Desktop/Самолет/Новое Внуково/выписки банка\\ЖК «Новое Внуково» Н_EscrowReport6_01.12.2022-08.01.2023.xlsx',
                    'СБЕР'),
                'ЖК «Новое Внуково» Н_EscrowReport7_01.12.2022-08.01.2023   д11.xlsx': (
                    'C:/Users/cyril/Desktop/Самолет/Новое Внуково/выписки банка\\ЖК «Новое Внуково» Н_EscrowReport7_01.12.2022-08.01.2023   д11.xlsx',
                    'СБЕР'),
                'ЖК «Новое Внуково» Н_EscrowReport8_01.12.2022-08.01.2023   д12.xlsx': (
                    'C:/Users/cyril/Desktop/Самолет/Новое Внуково/выписки банка\\ЖК «Новое Внуково» Н_EscrowReport8_01.12.2022-08.01.2023   д12.xlsx',
                    'СБЕР'),
                'ЖК «Новое Внуково» Н_EscrowReport9_01.12.2022-08.01.2023  д13.xlsx': (
                    'C:/Users/cyril/Desktop/Самолет/Новое Внуково/выписки банка\\ЖК «Новое Внуково» Н_EscrowReport9_01.12.2022-08.01.2023  д13.xlsx',
                    'СБЕР'),
                'ЖК Новое Внуково (до_EscrowReport13_01.12.2022-08.01.2023  д6.xlsx': (
                    'C:/Users/cyril/Desktop/Самолет/Новое Внуково/выписки банка\\ЖК Новое Внуково (до_EscrowReport13_01.12.2022-08.01.2023  д6.xlsx',
                    'СБЕР'),
                'ЖК Новое Внуково (до_EscrowReport14_01.12.2022-08.01.2023  д7.xlsx': (
                    'C:/Users/cyril/Desktop/Самолет/Новое Внуково/выписки банка\\ЖК Новое Внуково (до_EscrowReport14_01.12.2022-08.01.2023  д7.xlsx',
                    'СБЕР'),
                'ЖК Новое Внуково (до_EscrowReport15_01.12.2022-08.01.2023   д8.xlsx': (
                    'C:/Users/cyril/Desktop/Самолет/Новое Внуково/выписки банка\\ЖК Новое Внуково (до_EscrowReport15_01.12.2022-08.01.2023   д8.xlsx',
                    'СБЕР'),
                'ЖК Новое Внуково (до_EscrowReport16_01.12.2022-08.01.2023   д9.xlsx': (
                    'C:/Users/cyril/Desktop/Самолет/Новое Внуково/выписки банка\\ЖК Новое Внуково (до_EscrowReport16_01.12.2022-08.01.2023   д9.xlsx',
                    'СБЕР'),
                'ЖК Новое Внуково (до_EscrowReport17_01.12.2022-08.01.2023  д10.xlsx': (
                    'C:/Users/cyril/Desktop/Самолет/Новое Внуково/выписки банка\\ЖК Новое Внуково (до_EscrowReport17_01.12.2022-08.01.2023  д10.xlsx',
                    'СБЕР'),
                'ЖК Новое Внуково. Пе_EscrowReport18_01.12.2022-08.01.2023   д1.xlsx': (
                    'C:/Users/cyril/Desktop/Самолет/Новое Внуково/выписки банка\\ЖК Новое Внуково. Пе_EscrowReport18_01.12.2022-08.01.2023   д1.xlsx',
                    'СБЕР'),
                'ЖК Новое Внуково. Пе_EscrowReport19_01.12.2022-08.01.2023   д2.xlsx': (
                    'C:/Users/cyril/Desktop/Самолет/Новое Внуково/выписки банка\\ЖК Новое Внуково. Пе_EscrowReport19_01.12.2022-08.01.2023   д2.xlsx',
                    'СБЕР'),
                'ЖК Новое Внуково. Пе_EscrowReport20_01.12.2022-08.01.2023   д3.xlsx': (
                    'C:/Users/cyril/Desktop/Самолет/Новое Внуково/выписки банка\\ЖК Новое Внуково. Пе_EscrowReport20_01.12.2022-08.01.2023   д3.xlsx',
                    'СБЕР'),
                'ЖК Новое Внуково. Пе_EscrowReport21_01.12.2022-08.01.2023   д4.xlsx': (
                    'C:/Users/cyril/Desktop/Самолет/Новое Внуково/выписки банка\\ЖК Новое Внуково. Пе_EscrowReport21_01.12.2022-08.01.2023   д4.xlsx',
                    'СБЕР'),
                'ЖК Новое Внуково. Пе_EscrowReport22_01.12.2022-08.01.2023  д5.xlsx': (
                    'C:/Users/cyril/Desktop/Самолет/Новое Внуково/выписки банка\\ЖК Новое Внуково. Пе_EscrowReport22_01.12.2022-08.01.2023  д5.xlsx',
                    'СБЕР')
            },
            'check': False
        },
        'Прибрежный парк': {
            'bank_file': '',
            'bank_folder': r'C:\Users\cyril\Desktop\Самолет\Парк',
            'bank_name': ['СБЕР'],
            'single': True,
            'file_to_bank': {
                'Жилой комплекс по ад_EscrowReport1_01.12.2022-31.12.2022.xlsx': (
                    'C:/Users/cyril/Desktop/Самолет/Парк/выписки\\Жилой комплекс по ад_EscrowReport1_01.12.2022-31.12.2022.xlsx',
                    'СБЕР'),
                'Жилой комплекс по ад_EscrowReport2_01.12.2022-31.12.2022.xlsx': (
                    'C:/Users/cyril/Desktop/Самолет/Парк/выписки\\Жилой комплекс по ад_EscrowReport2_01.12.2022-31.12.2022.xlsx',
                    'СБЕР'),
                'Жилой комплекс по ад_EscrowReport3_01.12.2022-31.12.2022.xlsx': (
                    'C:/Users/cyril/Desktop/Самолет/Парк/выписки\\Жилой комплекс по ад_EscrowReport3_01.12.2022-31.12.2022.xlsx',
                    'СБЕР'),
                'ЖК Прибрежный парк 3_EscrowReport1_01.12.2022-31.12.2022.xlsx': (
                    'C:/Users/cyril/Desktop/Самолет/Парк/выписки\\ЖК Прибрежный парк 3_EscrowReport1_01.12.2022-31.12.2022.xlsx',
                    'СБЕР'),
                'ЖК Прибрежный парк 3_EscrowReport2_01.12.2022-31.12.2022.xlsx': (
                    'C:/Users/cyril/Desktop/Самолет/Парк/выписки\\ЖК Прибрежный парк 3_EscrowReport2_01.12.2022-31.12.2022.xlsx',
                    'СБЕР'),
                'ЖК Прибрежный парк к_EscrowReport10_01.12.2022-31.12.2022.xlsx': (
                    'C:/Users/cyril/Desktop/Самолет/Парк/выписки\\ЖК Прибрежный парк к_EscrowReport10_01.12.2022-31.12.2022.xlsx',
                    'СБЕР'),
                'ЖК Прибрежный парк к_EscrowReport11_01.12.2022-31.12.2022.xlsx': (
                    'C:/Users/cyril/Desktop/Самолет/Парк/выписки\\ЖК Прибрежный парк к_EscrowReport11_01.12.2022-31.12.2022.xlsx',
                    'СБЕР'),
                'ЖК Прибрежный парк к_EscrowReport12_01.12.2022-31.12.2022.xlsx': (
                    'C:/Users/cyril/Desktop/Самолет/Парк/выписки\\ЖК Прибрежный парк к_EscrowReport12_01.12.2022-31.12.2022.xlsx',
                    'СБЕР'),
                'ЖК Прибрежный парк к_EscrowReport13_01.12.2022-31.12.2022.xlsx': (
                    'C:/Users/cyril/Desktop/Самолет/Парк/выписки\\ЖК Прибрежный парк к_EscrowReport13_01.12.2022-31.12.2022.xlsx',
                    'СБЕР'),
                'ЖК Прибрежный парк к_EscrowReport14_01.12.2022-31.12.2022.xlsx': (
                    'C:/Users/cyril/Desktop/Самолет/Парк/выписки\\ЖК Прибрежный парк к_EscrowReport14_01.12.2022-31.12.2022.xlsx',
                    'СБЕР'),
                'ЖК Прибрежный парк к_EscrowReport15_01.12.2022-31.12.2022.xlsx': (
                    'C:/Users/cyril/Desktop/Самолет/Парк/выписки\\ЖК Прибрежный парк к_EscrowReport15_01.12.2022-31.12.2022.xlsx',
                    'СБЕР'),
                'ЖК Прибрежный парк к_EscrowReport16_01.12.2022-31.12.2022.xlsx': (
                    'C:/Users/cyril/Desktop/Самолет/Парк/выписки\\ЖК Прибрежный парк к_EscrowReport16_01.12.2022-31.12.2022.xlsx',
                    'СБЕР'),
                'ЖК Прибрежный парк к_EscrowReport6_01.12.2022-31.12.2022.xlsx': (
                    'C:/Users/cyril/Desktop/Самолет/Парк/выписки\\ЖК Прибрежный парк к_EscrowReport6_01.12.2022-31.12.2022.xlsx',
                    'СБЕР'),
                'ЖК Прибрежный парк к_EscrowReport7_01.12.2022-31.12.2022.xlsx': (
                    'C:/Users/cyril/Desktop/Самолет/Парк/выписки\\ЖК Прибрежный парк к_EscrowReport7_01.12.2022-31.12.2022.xlsx',
                    'СБЕР'),
                'ЖК Прибрежный парк к_EscrowReport8_01.12.2022-31.12.2022.xlsx': (
                    'C:/Users/cyril/Desktop/Самолет/Парк/выписки\\ЖК Прибрежный парк к_EscrowReport8_01.12.2022-31.12.2022.xlsx',
                    'СБЕР'),
                'ЖК Прибрежный парк к_EscrowReport9_01.12.2022-31.12.2022.xlsx': (
                    'C:/Users/cyril/Desktop/Самолет/Парк/выписки\\ЖК Прибрежный парк к_EscrowReport9_01.12.2022-31.12.2022.xlsx',
                    'СБЕР')
            },
            'check': False
        },
        'Пригород Лесное': {
            'bank_file': '',
            'bank_folder': r'C:\Users\cyril\Desktop\Самолет\Пригород',
            'bank_name': ['СБЕР'],
            'single': True,
            'file_to_bank': {
                '«ЖК Пригород Лесное»_EscrowReport10_01.12.2022-09.01.2023 8.2.xlsx': (
                    'C:/Users/cyril/Desktop/Самолет/Пригород/Выписки банка на 30.12\\«ЖК Пригород Лесное»_EscrowReport10_01.12.2022-09.01.2023 8.2.xlsx',
                    'СБЕР'),
                '«ЖК Пригород Лесное»_EscrowReport11_01.12.2022-09.01.2023 9.xlsx': (
                    'C:/Users/cyril/Desktop/Самолет/Пригород/Выписки банка на 30.12\\«ЖК Пригород Лесное»_EscrowReport11_01.12.2022-09.01.2023 9.xlsx',
                    'СБЕР'),
                '«ЖК Пригород Лесное»_EscrowReport12_01.12.2022-09.01.2023 7.1.xlsx': (
                    'C:/Users/cyril/Desktop/Самолет/Пригород/Выписки банка на 30.12\\«ЖК Пригород Лесное»_EscrowReport12_01.12.2022-09.01.2023 7.1.xlsx',
                    'СБЕР'),
                '«ЖК Пригород Лесное»_EscrowReport13_01.12.2022-09.01.2023 7.2.xlsx': (
                    'C:/Users/cyril/Desktop/Самолет/Пригород/Выписки банка на 30.12\\«ЖК Пригород Лесное»_EscrowReport13_01.12.2022-09.01.2023 7.2.xlsx',
                    'СБЕР'),
                '«ЖК Пригород Лесное»_EscrowReport14_01.12.2022-09.01.2023 10.1.xlsx': (
                    'C:/Users/cyril/Desktop/Самолет/Пригород/Выписки банка на 30.12\\«ЖК Пригород Лесное»_EscrowReport14_01.12.2022-09.01.2023 10.1.xlsx',
                    'СБЕР'),
                '«ЖК Пригород Лесное»_EscrowReport15_01.12.2022-09.01.2023 10.2.xlsx': (
                    'C:/Users/cyril/Desktop/Самолет/Пригород/Выписки банка на 30.12\\«ЖК Пригород Лесное»_EscrowReport15_01.12.2022-09.01.2023 10.2.xlsx',
                    'СБЕР'),
                '«ЖК Пригород Лесное»_EscrowReport9_01.12.2022-09.01.2023 8.1.xlsx': (
                    'C:/Users/cyril/Desktop/Самолет/Пригород/Выписки банка на 30.12\\«ЖК Пригород Лесное»_EscrowReport9_01.12.2022-09.01.2023 8.1.xlsx',
                    'СБЕР'),
                'ЖК Пригород Лесное 4_EscrowReport22_01.12.2022-09.01.2023 62.xlsx': (
                    'C:/Users/cyril/Desktop/Самолет/Пригород/Выписки банка на 30.12\\ЖК Пригород Лесное 4_EscrowReport22_01.12.2022-09.01.2023 62.xlsx',
                    'СБЕР'),
                'ЖК Пригород Лесное 4_EscrowReport23_01.12.2022-09.01.2023 63.xlsx': (
                    'C:/Users/cyril/Desktop/Самолет/Пригород/Выписки банка на 30.12\\ЖК Пригород Лесное 4_EscrowReport23_01.12.2022-09.01.2023 63.xlsx',
                    'СБЕР'),
                'ЖК Пригород Лесное 4_EscrowReport25_01.12.2022-09.01.2023 57.xlsx': (
                    'C:/Users/cyril/Desktop/Самолет/Пригород/Выписки банка на 30.12\\ЖК Пригород Лесное 4_EscrowReport25_01.12.2022-09.01.2023 57.xlsx',
                    'СБЕР'),
                'ЖК Пригород Лесное 4_EscrowReport26_01.12.2022-09.01.2023 58.xlsx': (
                    'C:/Users/cyril/Desktop/Самолет/Пригород/Выписки банка на 30.12\\ЖК Пригород Лесное 4_EscrowReport26_01.12.2022-09.01.2023 58.xlsx',
                    'СБЕР'),
                'ЖК Пригород Лесное 4_EscrowReport27_01.12.2022-09.01.2023 59.xlsx': (
                    'C:/Users/cyril/Desktop/Самолет/Пригород/Выписки банка на 30.12\\ЖК Пригород Лесное 4_EscrowReport27_01.12.2022-09.01.2023 59.xlsx',
                    'СБЕР'),
                'ЖК Пригород Лесное 4_EscrowReport28_01.12.2022-09.01.2023 60.xlsx': (
                    'C:/Users/cyril/Desktop/Самолет/Пригород/Выписки банка на 30.12\\ЖК Пригород Лесное 4_EscrowReport28_01.12.2022-09.01.2023 60.xlsx',
                    'СБЕР'),
                'ЖК Пригород Лесное 4_EscrowReport29_01.12.2022-09.01.2023 61.xlsx': (
                    'C:/Users/cyril/Desktop/Самолет/Пригород/Выписки банка на 30.12\\ЖК Пригород Лесное 4_EscrowReport29_01.12.2022-09.01.2023 61.xlsx',
                    'СБЕР'),
                'ЖК Пригород Лесное к_EscrowReport16_01.12.2022-09.01.2023 1.1.xlsx': (
                    'C:/Users/cyril/Desktop/Самолет/Пригород/Выписки банка на 30.12\\ЖК Пригород Лесное к_EscrowReport16_01.12.2022-09.01.2023 1.1.xlsx',
                    'СБЕР'),
                'ЖК Пригород Лесное к_EscrowReport17_01.12.2022-09.01.2023 1.2.xlsx': (
                    'C:/Users/cyril/Desktop/Самолет/Пригород/Выписки банка на 30.12\\ЖК Пригород Лесное к_EscrowReport17_01.12.2022-09.01.2023 1.2.xlsx',
                    'СБЕР'),
                'ЖК Пригород Лесное к_EscrowReport18_01.12.2022-09.01.2023 2.1.xlsx': (
                    'C:/Users/cyril/Desktop/Самолет/Пригород/Выписки банка на 30.12\\ЖК Пригород Лесное к_EscrowReport18_01.12.2022-09.01.2023 2.1.xlsx',
                    'СБЕР'),
                'ЖК Пригород Лесное к_EscrowReport19_01.12.2022-09.01.2023 2.2.xlsx': (
                    'C:/Users/cyril/Desktop/Самолет/Пригород/Выписки банка на 30.12\\ЖК Пригород Лесное к_EscrowReport19_01.12.2022-09.01.2023 2.2.xlsx',
                    'СБЕР'),
                'ЖК Пригород Лесное к_EscrowReport20_01.12.2022-09.01.2023 3.1.xlsx': (
                    'C:/Users/cyril/Desktop/Самолет/Пригород/Выписки банка на 30.12\\ЖК Пригород Лесное к_EscrowReport20_01.12.2022-09.01.2023 3.1.xlsx',
                    'СБЕР'),
                'ЖК Пригород Лесное к_EscrowReport21_01.12.2022-09.01.2023 3.2.xlsx': (
                    'C:/Users/cyril/Desktop/Самолет/Пригород/Выписки банка на 30.12\\ЖК Пригород Лесное к_EscrowReport21_01.12.2022-09.01.2023 3.2.xlsx',
                    'СБЕР'),
                'Комплексная жилая за_EscrowReport3_01.12.2022-09.01.2023.xlsx': (
                    'C:/Users/cyril/Desktop/Самолет/Пригород/Выписки банка на 30.12\\Комплексная жилая за_EscrowReport3_01.12.2022-09.01.2023.xlsx',
                    'СБЕР'),
                'Комплексная жилая за_EscrowReport4_01.12.2022-09.01.2023.xlsx': (
                    'C:/Users/cyril/Desktop/Самолет/Пригород/Выписки банка на 30.12\\Комплексная жилая за_EscrowReport4_01.12.2022-09.01.2023.xlsx',
                    'СБЕР'),
                'Комплексная жилая за_EscrowReport5_01.12.2022-09.01.2023 11.1.xlsx': (
                    'C:/Users/cyril/Desktop/Самолет/Пригород/Выписки банка на 30.12\\Комплексная жилая за_EscrowReport5_01.12.2022-09.01.2023 11.1.xlsx',
                    'СБЕР'),
                'Комплексная жилая за_EscrowReport6_01.12.2022-09.01.2023 11.2.xlsx': (
                    'C:/Users/cyril/Desktop/Самолет/Пригород/Выписки банка на 30.12\\Комплексная жилая за_EscrowReport6_01.12.2022-09.01.2023 11.2.xlsx',
                    'СБЕР'),
                'Комплексная жилая за_EscrowReport7_01.12.2022-09.01.2023 4.1.xlsx': (
                    'C:/Users/cyril/Desktop/Самолет/Пригород/Выписки банка на 30.12\\Комплексная жилая за_EscrowReport7_01.12.2022-09.01.2023 4.1.xlsx',
                    'СБЕР'),
                'Комплексная жилая за_EscrowReport8_01.12.2022-09.01.2023 4.2.xlsx': (
                    'C:/Users/cyril/Desktop/Самолет/Пригород/Выписки банка на 30.12\\Комплексная жилая за_EscrowReport8_01.12.2022-09.01.2023 4.2.xlsx',
                    'СБЕР'),
                'Пригород лесное корп_EscrowReport1_01.12.2022-09.01.2023.xlsx': (
                    'C:/Users/cyril/Desktop/Самолет/Пригород/Выписки банка на 30.12\\Пригород лесное корп_EscrowReport1_01.12.2022-09.01.2023.xlsx',
                    'СБЕР'),
                'Пригород Лесное корп_EscrowReport24_01.12.2022-09.01.2023 5.1.xlsx': (
                    'C:/Users/cyril/Desktop/Самолет/Пригород/Выписки банка на 30.12\\Пригород Лесное корп_EscrowReport24_01.12.2022-09.01.2023 5.1.xlsx',
                    'СБЕР'),
                'Пригород Лесное корп_EscrowReport2_01.12.2022-09.01.2023 5.2.xlsx': (
                    'C:/Users/cyril/Desktop/Самолет/Пригород/Выписки банка на 30.12\\Пригород Лесное корп_EscrowReport2_01.12.2022-09.01.2023 5.2.xlsx',
                    'СБЕР')
            },
            'check': False
        },
        'Пятницкие кварталы': {
            'bank_file': '',
            'bank_folder': r'C:\Users\cyril\Desktop\Самолет\Пятницкие кварталы',
            'bank_name': ['СБЕР'],
            'single': True,
            'file_to_bank': {
                '1-Пятницкие Луга корпу_EscrowReport2_01.12.2022-31.12.2022.xlsx': (
                    'C:/Users/cyril/Desktop/Самолет/Пятницкие кварталы/выписки банка\\1-Пятницкие Луга корпу_EscrowReport2_01.12.2022-31.12.2022.xlsx',
                    'СБЕР'),
                '2-Пятницкие Луга корпу_EscrowReport3_01.12.2022-31.12.2022.xlsx': (
                    'C:/Users/cyril/Desktop/Самолет/Пятницкие кварталы/выписки банка\\2-Пятницкие Луга корпу_EscrowReport3_01.12.2022-31.12.2022.xlsx',
                    'СБЕР'),
                '2.2-Пятницкие луга Компл_EscrowReport1_01.12.2022-31.12.2022.xlsx': (
                    'C:/Users/cyril/Desktop/Самолет/Пятницкие кварталы/выписки банка\\2.2-Пятницкие луга Компл_EscrowReport1_01.12.2022-31.12.2022.xlsx',
                    'СБЕР')
            },
            'check': False
        },
        'Тропарево Парк': {
            'bank_file': '',
            'bank_folder': r'C:\Users\cyril\Desktop\Самолет\Тропарево',
            'bank_name': '',
            'single': True,
            'file_to_bank': {
                'ЖК Тропарево Парк (к_EscrowReport1_17.12.2022-31.12.2022 2.1.xlsx': (
                    'C:/Users/cyril/Desktop/Самолет/Тропарево/Выписки банка\\ЖК Тропарево Парк (к_EscrowReport1_17.12.2022-31.12.2022 2.1.xlsx',
                    'СБЕР'),
                'ЖК Тропарево Парк (к_EscrowReport2_17.12.2022-31.12.2022 2.2.xlsx': (
                    'C:/Users/cyril/Desktop/Самолет/Тропарево/Выписки банка\\ЖК Тропарево Парк (к_EscrowReport2_17.12.2022-31.12.2022 2.2.xlsx',
                    'СБЕР'),
                'ЖК Тропарево Парк (к_EscrowReport4_17.12.2022-31.12.2022 2.4.xlsx': (
                    'C:/Users/cyril/Desktop/Самолет/Тропарево/Выписки банка\\ЖК Тропарево Парк (к_EscrowReport4_17.12.2022-31.12.2022 2.4.xlsx',
                    'СБЕР'),
                'ЖК Тропарево Парк (к_EscrowReport6_17.12.2022-31.12.2022 1.1.xlsx': (
                    'C:/Users/cyril/Desktop/Самолет/Тропарево/Выписки банка\\ЖК Тропарево Парк (к_EscrowReport6_17.12.2022-31.12.2022 1.1.xlsx',
                    'СБЕР'),
                'ЖК Тропарево Парк (к_EscrowReport7_17.12.2022-31.12.2022 1.2.xlsx': (
                    'C:/Users/cyril/Desktop/Самолет/Тропарево/Выписки банка\\ЖК Тропарево Парк (к_EscrowReport7_17.12.2022-31.12.2022 1.2.xlsx',
                    'СБЕР'),
                'ЖК Тропарево Парк (к_EscrowReport8_17.12.2022-31.12.2022 1.3.xlsx': (
                    'C:/Users/cyril/Desktop/Самолет/Тропарево/Выписки банка\\ЖК Тропарево Парк (к_EscrowReport8_17.12.2022-31.12.2022 1.3.xlsx',
                    'СБЕР')
            },
            'check': False
        },
    }

    control_bank_sum_dict = {'Алхимово':8509794618, 'Верейская': 12059017028.80, 'Горки Парк':12059017029, 'Долина Яузы':350353025.09,
                                'Егорово Парк':6682206331, 'Заречье':3192104891.34 , 'Иванкино': 132667226.6, 'Лайково': 431609857,
                                'Люберцы': 23158377671,'Молжаниново':10895665231 ,'Мытищи': 23761219517,'Новоданиловская': 7498683812,
                                'Остафьево': 10188066743, 'Путилково': 10124119272, 'Спутник': 12675335569.63,
                                'Новое Внуково':  18734688940.74 ,'Прибрежный парк':16330258012 ,'Пригород Лесное':  29021512005.04 ,
                                'Пятницкие кварталы':4616973870 ,'Тропарево Парк': 9052780744, 'Томилино':  17367622357, 'Некрасовка':7873627726}

    def test_old_bank(self):
        for key, value in self.bank_file_dict.items():
            account = AccountFile(self.account_file_dict[key])
            print(key)
            bank = BankFile(value, account.type_dict)
            number = bank.document_sum
            self.assertEqual(round(number), round(self.control_bank_sum_dict[key]))
    #

    def test_old_account(self):
        for key, value in self.account_file_dict.items():
            print(key)
            number = AccountFile(value).document_sum
            self.assertEqual(round(number), round(self.control_account_sum_dict[key]))

    ################################################################################################

    new_bank_file_dict = {
        'Алхимово': {
            'bank_file': r"C:\Users\cyril\Desktop\Самолет\НОВЫЕ ОТЧЕТЫ\Сверка на 31.03.2023г\Алхимово (R)\Алхимово общий отчет-01.03.2023-31.03.2023.xlsx",
            'bank_folder': '',
            'bank_name': ['СБЕР'],
            'single': True,
            'file_to_bank': dict(),
            'check': False
        },
        'Томилино': {
            'bank_file': r"C:\Users\cyril\Desktop\Самолет\НОВЫЕ ОТЧЕТЫ\Сверка на 31.03.2023г\Томилино\CommonDeveloper_01.04.2023_5027240182.xlsx",
            'bank_folder': '',
            'bank_name': ['ВТБ'],
            'single': True,
            'file_to_bank': dict(),
            'check': False
        },
        # 'Верейская': {
        #     'bank_file': r"C:\Users\cyril\Desktop\Самолет\НОВЫЕ ОТЧЕТЫ\Сверка на 31.03.2023г\Верейская 41\31.03.2023.xlsx",
        #     'bank_folder': '',
        #     'bank_name': ['МКБ'],
        #     'single': True,
        #     'file_to_bank': dict(),
        #     'check': False
        # },
        'Горки Парк': {
            'bank_file': r"C:\Users\cyril\Desktop\Самолет\НОВЫЕ ОТЧЕТЫ\Сверка на 31.03.2023г\Горки Парк, Сам-Коробово (R)\Отчёт 31.03.2023.xlsx",
            'bank_folder': '',
            'bank_name': ['СБЕР'],
            'single': True,
            'file_to_bank': dict(),
            'check': False
        },
        'Егорово Парк': {
            'bank_file': r"C:\Users\cyril\Desktop\Самолет\НОВЫЕ ОТЧЕТЫ\Сверка на 31.03.2023г\Егорово Парк, Сам-Жилино (R)\EscrowBalanceReports_01.03.2023-31.03.2023.xlsx",
            'bank_folder': r'',
            'bank_name': ['СБЕР'],
            'single': True,
            'file_to_bank': dict(),
            'check': False
        },
        'Заречье': {
            'bank_file': r"C:\Users\cyril\Desktop\Самолет\НОВЫЕ ОТЧЕТЫ\Сверка на 31.03.2023г\Заречье\ООО СЗ Самолет-Заречье 01.01.2019 - 31.03.2023.xlsx",
            'bank_folder': '',
            'bank_name': ['Совкомбанк'],
            'single': True,
            'file_to_bank': dict(),
            'check': False
        },
        # 'Иванкино': {
        #     'bank_file': r"C:\Users\cyril\Desktop\Самолет\НОВЫЕ ОТЧЕТЫ\Сверка на 31.03.2023г\Квартал Иванкино (Самолёт-Олимп)\31.03.2023.xlsx",
        #     'bank_folder': '',
        #     'bank_name': ['МКБ'],
        #     'single': True,
        #     'file_to_bank': dict(),
        #     'check': False
        # },
        'Лайково': {
            'bank_file': r"C:\Users\cyril\Desktop\Самолет\НОВЫЕ ОТЧЕТЫ\Сверка на 31.03.2023г\Лайково\Выписки\Счета ЭСКРОУ_1043532145_2023-03-31.xlsx",
            'bank_folder': '',
            'bank_name': ['Дом РФ'],
            'single': True,
            'file_to_bank': dict(),
            'check': False
        },
        'Люберцы': {
            'bank_file': r"C:\Users\cyril\Desktop\Самолет\НОВЫЕ ОТЧЕТЫ\Сверка на 31.03.2023г\Люберцы\Люб месяц.XLSX",
            'bank_folder': '',
            'bank_name': ['Альфа Банк'],
            'single': True,
            'file_to_bank': dict(),
            'check': False
        },
        # 'Молжаниново': {
        #     'bank_file': r"C:\Users\cyril\Desktop\Самолет\НОВЫЕ ОТЧЕТЫ\Сверка на 31.03.2023г\Молжаниново\31.03.2023.xlsx",
        #     'bank_folder': '',
        #     'bank_name': ['МКБ'],
        #     'single': True,
        #     'file_to_bank': dict(),
        #     'check': False
        # },
        'Мытищи': {
            'bank_file': r"C:\Users\cyril\Desktop\Самолет\НОВЫЕ ОТЧЕТЫ\Сверка на 31.03.2023г\Мытищи Парк (Самолет-Мытищи)\МЫТИЩИ месяц.XLSX",
            'bank_folder': '',
            'bank_name': ['Альфа Банк'],
            'single': True,
            'file_to_bank': dict(),
            'check': False
        },
        'Новоданиловская': {
            'bank_file': r"C:\Users\cyril\Desktop\Самолет\НОВЫЕ ОТЧЕТЫ\Сверка на 31.03.2023г\Новоданиловская 8\Счета ЭСКРОУ_850474049_2023-03-31.xlsx",
            'bank_folder': '',
            'bank_name': ['Дом РФ'],
            'single': True,
            'file_to_bank': dict(),
            'check': False
        },
        'Остафьево': {
            'bank_file': r"C:\Users\cyril\Desktop\Самолет\НОВЫЕ ОТЧЕТЫ\Сверка на 31.03.2023г\Остафьево (СР-Групп)\CommonDeveloper_01.04.2023_7731319243.xlsx",
            'bank_folder': '',
            'bank_name': ['ВТБ'],
            'single': True,
            'file_to_bank': dict(),
            'check': False
        },
        'Путилково': {
            'bank_file': '',
            'bank_folder': r'C:\Users\cyril\Desktop\Самолет\НОВЫЕ ОТЧЕТЫ\Сверка на 31.03.2023г\Путилково\Выписки"',
            'bank_name': ['ГПБ'],
            'single': True,
            'file_to_bank': {
                'Путилково 31.03.23-1.xlsx': (
                    r"C:\Users\cyril\Desktop\Самолет\НОВЫЕ ОТЧЕТЫ\Сверка на 31.03.2023г\Путилково\Выписки\Путилково 31.03.23-1.xlsx",
                    'ГПБ'),
                'Путилково 31.03.23-2.xlsx': (
                    r"C:\Users\cyril\Desktop\Самолет\НОВЫЕ ОТЧЕТЫ\Сверка на 31.03.2023г\Путилково\Выписки\Путилково 31.03.23-2.xlsx",
                    'ГПБ')
            },
            'check': False
        },
        'Спутник': {
            'bank_file': '',
            'bank_folder': r'C:\Users\cyril\Desktop\Самолет\НОВЫЕ ОТЧЕТЫ\Сверка на 31.03.2023г\Спутник\Выписки',
            'bank_name': '',
            'single': False,
            'file_to_bank': {
                'отчет эскроу дом рф 02.04.2023.xlsx': (
                    r"C:\Users\cyril\Desktop\Самолет\НОВЫЕ ОТЧЕТЫ\Сверка на 31.03.2023г\Спутник\Выписки\отчет эскроу дом рф 02.04.2023.xlsx",
                    'Дом РФ'),
                'отчет эскроу совком 31.03.2023.xlsx': (
                    r"C:\Users\cyril\Desktop\Самолет\НОВЫЕ ОТЧЕТЫ\Сверка на 31.03.2023г\Спутник\Выписки\отчет эскроу совком 31.03.2023.xlsx",
                    'Совкомбанк')
            },
            'check': False
        },
        'Новое Внуково': {
            'bank_file': r"C:\Users\cyril\Desktop\Самолет\НОВЫЕ ОТЧЕТЫ\Сверка на 31.03.2023г\Новое Внуково, Санино 1 (R)\EscrowBalanceReports_01.03.2023-31.03.2023.xlsx",
            'bank_folder': r'',
            'bank_name': ['СБЕР'],
            'single': True,
            'file_to_bank': dict(),
            'check': False
        },
        'Прибрежный парк': {
            'bank_file': r"C:\Users\cyril\Desktop\Самолет\НОВЫЕ ОТЧЕТЫ\Сверка на 31.03.2023г\Прибрежный парк (R)\EscrowBalanceReports_01.03.2023-31.03.2023.xlsx",
            'bank_folder': r'',
            'bank_name': ['СБЕР'],
            'single': True,
            'file_to_bank': dict(),
            'check': False
        },
        'Пригород Лесное': {
            'bank_file': r"C:\Users\cyril\Desktop\Самолет\НОВЫЕ ОТЧЕТЫ\Сверка на 31.03.2023г\Пригород Лесное  (R)\EscrowBalanceReports_01.03.2023-31.03.2023.xlsx",
            'bank_folder': '',
            'bank_name': ['СБЕР'],
            'single': True,
            'file_to_bank': dict(),
            'check': False
        },
        'Пятницкие кварталы': {
            'bank_file': r"C:\Users\cyril\Desktop\Самолет\НОВЫЕ ОТЧЕТЫ\Сверка на 31.03.2023г\Пятницкие луга (Юрлово) (R)\Юрлово общий отчет-01.03.2023-31.03.2023.xlsx",
            'bank_folder': '',
            'bank_name': ['СБЕР'],
            'single': True,
            'file_to_bank': dict(),
            'check': False
        },
        'Тропарево Парк': {
            'bank_file': r"C:\Users\cyril\Desktop\Самолет\НОВЫЕ ОТЧЕТЫ\Сверка на 31.03.2023г\Тропарёво Парк, Сам-Дудкино (R)\EscrowBalanceReports_01.03.2023-31.03.2023.xlsx",
            'bank_folder': '',
            'bank_name': ['СБЕР'],
            'single': True,
            'file_to_bank': dict(),
            'check': False
        },
        'Сабурово': {
            'bank_file': r"C:\Users\cyril\Desktop\Самолет\НОВЫЕ ОТЧЕТЫ\Сверка на 31.03.2023г\Сабурово-1\Отчет эскроу 31.03.23.xlsx",
            'bank_folder': '',
            'bank_name': ['ГПБ'],
            'single': True,
            'file_to_bank': dict(),
            'check': False
        },
        'Долина Яузы': {
            'bank_file': r"C:\Users\cyril\Desktop\Самолет\НОВЫЕ ОТЧЕТЫ\Сверка на 31.03.2023г\Долина Яузы (СЗ Реновация Мытищи)\РМ месяц.XLSX",
            'bank_folder': '',
            'bank_name': ['Альфа Банк'],
            'single': True,
            'file_to_bank': dict(),
            'check': False
        },

        'Квартал Западный': {
            'bank_file': r"C:\Users\cyril\Desktop\Самолет\НОВЫЕ ОТЧЕТЫ\Сверка на 31.03.2023г\Квартал Западный\КЗ месяц.XLSX",
            'bank_folder': '',
            'bank_name': ['Альфа Банк'],
            'single': True,
            'file_to_bank': dict(),
            'check': False
        },

        'Новое Видное': {
            'bank_file': '',
            'bank_folder': r'C:\Users\cyril\Desktop\Самолет\НОВЫЕ ОТЧЕТЫ\Сверка на 31.03.2023г\Новое Видное - Калиновка\Выписки',
            'bank_name': '',
            'single': True,
            'file_to_bank': {
                'Отчет Калиновка 0104-(1).xlsx': (
                    r"C:\Users\cyril\Desktop\Самолет\НОВЫЕ ОТЧЕТЫ\Сверка на 31.03.2023г\Новое Видное - Калиновка\Выписки\Отчет Калиновка 0104-(1).xlsx",
                    'ГПБ'),
                'Отчет Калиновка 0104-(2).xlsx': (
                    r"C:\Users\cyril\Desktop\Самолет\НОВЫЕ ОТЧЕТЫ\Сверка на 31.03.2023г\Новое Видное - Калиновка\Выписки\Отчет Калиновка 0104-(2).xlsx",
                    'ГПБ')
            },
            'check': False
        },

    }

    new_control_bank_sum_dict = {'Алхимово': 8509794617.93, 'Верейская': 3242654167, 'Горки Парк': 14734326671.63,
                             'Долина Яузы': 513764655,
                             'Егорово Парк': 7622744037.63, 'Заречье': 3916465446.16, 'Иванкино': 466764366.1,
                             'Лайково': 1099184901.69,
                             'Люберцы': 15482467989, 'Молжаниново': 13549274022, 'Мытищи': 19518412193,
                             'Новоданиловская': 7881975276,
                             'Остафьево': 10560598756.83, 'Путилково': 22110559968, 'Спутник': 11049558741.00,
                             'Новое Внуково': 14661311482.84, 'Прибрежный парк': 19280212387.45,
                             'Пригород Лесное': 30210452062.88,
                             'Пятницкие кварталы': 5636631196.88, 'Тропарево Парк': 10428259337.10, 'Томилино': 19274389667.30,
                             'Сабурово': 132014609, 'Квартал Западный': 206050296.7,'Новое Видное': 576420296
    }
    new_account_file_dict = \
        {
            'Алхимово': {
                'account': r"C:\Users\cyril\Desktop\Самолет\НОВЫЕ ОТЧЕТЫ\Сверка на 31.03.2023г\Алхимово (R)\ОСВ по счету 009.СЭ за ... - 1 квартал 2023 г.АЛХИМОВО.xlsx",
                'bank_name': ['СБЕР'],
                'type': True,
                'check_nomenclature': True,
                'check_account': False
            },
            'Томилино': {
                'account': r"C:\Users\cyril\Desktop\Самолет\НОВЫЕ ОТЧЕТЫ\Сверка на 31.03.2023г\Томилино\Оборотно-сальдовая ведомость по счету 009.СЭ САМОЛЕТ-ТОМИЛИНО.xlsx",
                'bank_name': ['ВТБ'],
                'type': True,
                'check_nomenclature': True,
                'check_account': False
            },
            'Верейская': {
                'account': r"C:\Users\cyril\Desktop\Самолет\НОВЫЕ ОТЧЕТЫ\Сверка на 31.03.2023г\Верейская 41\Оборотно-сальдовая ведомость по счету 009.СЭ  СЗ  САМОЛЕТ-ВЕРЕЙСКАЯ.xlsx",
                'bank_name': ['МКБ'],
                'type': True,
                'check_nomenclature': True,
                'check_account': False
            },
            'Горки Парк': {
                'account': r"C:\Users\cyril\Desktop\Самолет\НОВЫЕ ОТЧЕТЫ\Сверка на 31.03.2023г\Горки Парк, Сам-Коробово (R)\ОСВ по счету 009.СЭ СЗ  САМОЛЕТ-КОРОБОВО.xlsx",
                'bank_name': ['СБЕР'],
                'type': True,
                'check_nomenclature': True,
                'check_account': False

            },
            'Егорово Парк': {
                'account': r"C:\Users\cyril\Desktop\Самолет\НОВЫЕ ОТЧЕТЫ\Сверка на 31.03.2023г\Егорово Парк, Сам-Жилино (R)\ОСВ по счету 009.СЭ СЗ  САМОЛЕТ-ЖИЛИНО.xlsx",
                'bank_name': ['СБЕР'],
                'type': True,
                'check_nomenclature': True,
                'check_account': False
            },
            'Заречье': {
                'account': r"C:\Users\cyril\Desktop\Самолет\НОВЫЕ ОТЧЕТЫ\Сверка на 31.03.2023г\Заречье\Оборотно-сальдовая ведомость по счету 009.СЭ САМОЛЕТ-ЗАРЕЧЬЕ.xlsx",
                'bank_name': ['Совкомбанк'],
                'type': True,
                'check_nomenclature': True,
                'check_account': False
            },
            'Иванкино': {
                'account': r"C:\Users\cyril\Desktop\Самолет\НОВЫЕ ОТЧЕТЫ\Сверка на 31.03.2023г\Квартал Иванкино (Самолёт-Олимп)\ОСВ по счету 009.СЭ САМОЛЕТ-ОЛИМП.xlsx",
                'bank_name': ['МКБ'],
                'type': True,
                'check_nomenclature': True,
                'check_account': False
            },
            'Лайково': {
                'account': r"C:\Users\cyril\Desktop\Самолет\НОВЫЕ ОТЧЕТЫ\Сверка на 31.03.2023г\Лайково\Оборотно-сальдовая ведомость по счету 009.СЭ САМОЛЕТ-ЛАЙКОВО.xlsx",
                'bank_name': ['Дом РФ'],
                'type': True,
                'check_nomenclature': True,
                'check_account': False
            },
            'Люберцы': {
                'account': r"C:\Users\cyril\Desktop\Самолет\НОВЫЕ ОТЧЕТЫ\Сверка на 31.03.2023г\Люберцы\Оборотно-сальдовая ведомость по счету 009.СЭ САМОЛЕТ ДЕВЕЛОПМЕНТ.xlsx",
                'bank_name': ['Альфа Банк'],
                'type': True,
                'check_nomenclature': True,
                'check_account': False

            },
            'Молжаниново': {
                'account': r"C:\Users\cyril\Desktop\Самолет\НОВЫЕ ОТЧЕТЫ\Сверка на 31.03.2023г\Молжаниново\Оборотно-сальдовая ведомость по счету 009.СЭ САМОЛЕТ-МОЛЖАНИНОВО.xlsx",
                'bank_name': ['МКБ'],
                'type': True,
                'check_nomenclature': True,
                'check_account': False
            },
            'Мытищи': {
                'account': r"C:\Users\cyril\Desktop\Самолет\НОВЫЕ ОТЧЕТЫ\Сверка на 31.03.2023г\Мытищи Парк (Самолет-Мытищи)\Оборотно-сальдовая ведомость по счету 009.СЭ САМОЛЕТ-МЫТИЩИ.xlsx",
                'bank_name': ['Альфа Банк'],
                'type': True,
                'check_nomenclature': True,
                'check_account': False
            },
            'Новоданиловская': {
                'account': r"C:\Users\cyril\Desktop\Самолет\НОВЫЕ ОТЧЕТЫ\Сверка на 31.03.2023г\Новоданиловская 8\Оборотно-сальдовая ведомость по счету 009.СЭ ДМ АПАРТМЕНТС.xlsx",
                'bank_name': ['Дом РФ'],
                'type': True,
                'check_nomenclature': True,
                'check_account': False
            },
            'Остафьево': {
                'account': r"C:\Users\cyril\Desktop\Самолет\НОВЫЕ ОТЧЕТЫ\Сверка на 31.03.2023г\Остафьево (СР-Групп)\Оборотно-сальдовая ведомость по счету 009.СЭ СР-ГРУПП.xlsx",
                'bank_name': ['ВТБ'],
                'type': True,
                'check_nomenclature': True,
                'check_account': False
            },
            'Путилково': {
                'account': r"C:\Users\cyril\Desktop\Самолет\НОВЫЕ ОТЧЕТЫ\Сверка на 31.03.2023г\Путилково\Оборотно-сальдовая ведомость по счету 009.СЭ САМОЛЕТ-ПУТИЛКОВО.xlsx",
                'bank_name': ['ГПБ'],
                'type': True,
                'check_nomenclature': True,
                'check_account': False
            },
            'Новое Внуково': {
                'account': r"C:\Users\cyril\Desktop\Самолет\НОВЫЕ ОТЧЕТЫ\Сверка на 31.03.2023г\Новое Внуково, Санино 1 (R)\Оборотно-сальдовая ведомость по счету 009.СЭ СЗ  САНИНО 1.xlsx",
                'bank_name': ['СБЕР'],
                'type': True,
                'check_nomenclature': True,
                'check_account': False
            },
            'Прибрежный парк': {
                'account': r"C:\Users\cyril\Desktop\Самолет\НОВЫЕ ОТЧЕТЫ\Сверка на 31.03.2023г\Прибрежный парк (R)\ОСВ по счету 009.СЭ СЗ  ПРИБРЕЖНЫЙ ПАРК.xlsx",
                'bank_name': ['СБЕР'],
                'type': True,
                'check_nomenclature': True,
                'check_account': False
            },
            'Пригород Лесное': {
                'account': r"C:\Users\cyril\Desktop\Самолет\НОВЫЕ ОТЧЕТЫ\Сверка на 31.03.2023г\Пригород Лесное  (R)\Оборотно-сальдовая ведомость по счету 009.СЭ ПРИГОРОД ЛЕСНОЕ.xlsx",
                'bank_name': ['СБЕР'],
                'type': True,
                'check_nomenclature': True,
                'check_account': False
            },
            'Пятницкие кварталы': {
                'account': r"C:\Users\cyril\Desktop\Самолет\НОВЫЕ ОТЧЕТЫ\Сверка на 31.03.2023г\Пятницкие луга (Юрлово) (R)\ОСВ по счету 009.СЭ САМОЛЕТ-ЮРЛОВО.xlsx",
                'bank_name': ['СБЕР'],
                'type': True,
                'check_nomenclature': True,
                'check_account': False
            },
            'Спутник': {
                'account': r"C:\Users\cyril\Desktop\Самолет\НОВЫЕ ОТЧЕТЫ\Сверка на 31.03.2023г\Спутник\Оборотно-сальдовая ведомость по счету 009.СЭ СЗ  БУХТА ЛЭНД.xlsx",
                'bank_name': ['ПСБ'],
                'type': True,
                'check_nomenclature': True,
                'check_account': False
            },
            'Тропарево Парк': {
                'account': r"C:\Users\cyril\Desktop\Самолет\НОВЫЕ ОТЧЕТЫ\Сверка на 31.03.2023г\Тропарёво Парк, Сам-Дудкино (R)\Оборотно-сальдовая ведомость по счету 009.СЭ САМОЛЕТ-ДУДКИНО.xlsx",
                'bank_name': ['СБЕР'],
                'type': True,
                'check_nomenclature': True,
                'check_account': False
            },
            'Сабурово': {
                'account': r"C:\Users\cyril\Desktop\Самолет\НОВЫЕ ОТЧЕТЫ\Сверка на 31.03.2023г\Сабурово-1\Оборотно-сальдовая ведомость по счету 009.СЭ САМОЛЕТ-САБУРОВО-1.xlsx",
                'bank_name': ['ГПБ'],
                'type': True,
                'check_nomenclature': True,
                'check_account': False
            },
            'Долина Яузы': {
                'account': r"C:\Users\cyril\Desktop\Самолет\НОВЫЕ ОТЧЕТЫ\Сверка на 31.03.2023г\Долина Яузы (СЗ Реновация Мытищи)\Оборотно-сальдовая ведомость по счету 009.СЭ СЗ  РЕНОВАЦИЯ-МЫТИЩИ.xlsx",
                'bank_name': ['Альфа Банк'],
                'type': True,
                'check_nomenclature': True,
                'check_account': False
            },
            'Квартал Западный': {
                'account': r"C:\Users\cyril\Desktop\Самолет\НОВЫЕ ОТЧЕТЫ\Сверка на 31.03.2023г\Квартал Западный\Оборотно-сальдовая ведомость по счету 009.СЭ САМОЛЕТ-КВАРТАЛ ЗАПАДНЫЙ.xlsx",
                'bank_name': ['Альфа Банк'],
                'type': True,
                'check_nomenclature': True,
                'check_account': False
            },
            'Новое Видное': {
                'account': r"C:\Users\cyril\Desktop\Самолет\НОВЫЕ ОТЧЕТЫ\Сверка на 31.03.2023г\Новое Видное - Калиновка\Оборотно-сальдовая ведомость по счету 009.СЭ САМОЛЕТ-КАЛИНОВКА.xlsx",
                'bank_name': ['ГПБ'],
                'type': True,
                'check_nomenclature': True,
                'check_account': False
            }
        }

    new_control_account_sum_dict = {'Алхимово': 8674530750.20, 'Верейская': 2418735830.52, 'Горки Парк': 14734326671.63,
                        'Долина Яузы': 513764655.45,
                        'Егорово Парк': 7612547337.78, 'Заречье': 7288206666.91, 'Иванкино': 443551823.95,
                        'Лайково': 1099184901.69,
                        'Люберцы': 15478774948.87, 'Молжаниново': 12223529546.32, 'Мытищи': 20094268890.83,
                        'Новоданиловская': 7881975276.25,
                        'Остафьево': 10560598756.83, 'Путилково': 11013151651.59, 'Новое Внуково': 14661311482.92,
                        'Прибрежный парк': 19280212387.45,
                        'Пригород Лесное': 30243644354.83, 'Пятницкие кварталы': 5637486491.07,
                        'Спутник': 13119588751.36, 'Тропарево Парк': 10429392326.14, 'Томилино': 19081309990.91,
                        'Сабурово': 132014608.58,'Квартал Западный': 206050296.73, 'Новое Видное':288210147.84
                                    }
    def test_new_bank(self):
        for key, value in self.new_bank_file_dict.items():
            account = AccountFile(self.new_account_file_dict[key])
            print(key)
            bank = BankFile(value, account.type_dict)
            number = bank.document_sum
            self.assertEqual(round(number), round(self.new_control_bank_sum_dict[key]))
    #

    def test_new_account(self):
        for key, value in self.new_account_file_dict.items():
            number = AccountFile(value).document_sum
            self.assertEqual(round(number), round(self.new_control_account_sum_dict[key]))


##############################################################################################################
    new_new_bank_file_dict = {
        'Алхимово': {
            'bank_file': r"C:\Users\cyril\Desktop\Самолет\3. Ревью на 30.04.2023г\Алхимово\Алхимово общий отчет 01.04.2023-30.04.2023.XLSX",
            'bank_folder': '',
            'bank_name': ['СБЕР'],
            'single': True,
            'file_to_bank': dict(),
            'check': False
        },
        'Томилино': {
            'bank_file': r"C:\Users\cyril\Desktop\Самолет\3. Ревью на 30.04.2023г\Томилино +\CommonDeveloper_01.05.2023_5027240182.xlsx",
            'bank_folder': '',
            'bank_name': ['ВТБ'],
            'single': True,
            'file_to_bank': dict(),
            'check': False
        },
        'Верейская': {
            'bank_file': r"C:\Users\cyril\Desktop\Самолет\3. Ревью на 30.04.2023г\Верейская 41 +\02.05.2023.xlsx",
            'bank_folder': '',
            'bank_name': ['МКБ'],
            'single': True,
            'file_to_bank': dict(),
            'check': False
        },
        'Горки Парк': {
            'bank_file': r"C:\Users\cyril\Desktop\Самолет\3. Ревью на 30.04.2023г\Горки Парк, Сам-Коробово\EscrowBalanceReports_01.04.2023-30.04.2023.XLSX",
            'bank_folder': '',
            'bank_name': ['СБЕР'],
            'single': True,
            'file_to_bank': dict(),
            'check': False
        },
        'Егорово Парк': {
            'bank_file': r"C:\Users\cyril\Desktop\Самолет\3. Ревью на 30.04.2023г\Егорово Парк, Сам-Жилино\EscrowBalanceReports_01.04.2023-30.04.2023 (1).XLSX",
            'bank_folder': r'',
            'bank_name': ['СБЕР'],
            'single': True,
            'file_to_bank': dict(),
            'check': False
        },
        'Заречье': {
            'bank_file': r"C:\Users\cyril\Desktop\Самолет\3. Ревью на 30.04.2023г\Заречье +-\Банк\ООО СЗ Самолет-Заречье 01.01.2019 - 31.03.2023.xlsx",
            'bank_folder': '',
            'bank_name': ['Совкомбанк'],
            'single': True,
            'file_to_bank': dict(),
            'check': False
        },
        'Иванкино': {
            'bank_file': r"C:\Users\cyril\Desktop\Самолет\3. Ревью на 30.04.2023г\Квартал Иванкино (Самолёт-Олимп) +\30.04.2023.xlsx",
            'bank_folder': '',
            'bank_name': ['МКБ'],
            'single': True,
            'file_to_bank': dict(),
            'check': False
        },
        # 'Лайково': {
        #     'bank_file': r"C:\Users\cyril\Desktop\Самолет\НОВЫЕ ОТЧЕТЫ\Сверка на 31.03.2023г\Лайково\Выписки\Счета ЭСКРОУ_1043532145_2023-03-31.xlsx",
        #     'bank_folder': '',
        #     'bank_name': ['Дом РФ'],
        #     'single': True,
        #     'file_to_bank': dict(),
        #     'check': False
        # },
        'Люберцы': {
            'bank_file': r"C:\Users\cyril\Desktop\Самолет\3. Ревью на 30.04.2023г\Люберцы +\ООО СЗ САМОЛЕТ ДЕВЕЛОПМЕНТ 28.04.2023-01.05.2023 .xlsx",
            'bank_folder': '',
            'bank_name': ['Альфа Банк'],
            'single': True,
            'file_to_bank': dict(),
            'check': False
        },
        'Молжаниново': {
            'bank_file': r"C:\Users\cyril\Desktop\Самолет\3. Ревью на 30.04.2023г\Молжаниново +\02.05.2023.xlsx",
            'bank_folder': '',
            'bank_name': ['МКБ'],
            'single': True,
            'file_to_bank': dict(),
            'check': False
        },
        'Мытищи': {
            'bank_file': r"C:\Users\cyril\Desktop\Самолет\3. Ревью на 30.04.2023г\Мытищи Парк (Самолет-Мытищи) +\ООО СЗ САМОЛЕТ-МЫТИЩИ 28.04.2023-01.05.2023 .xlsx",
            'bank_folder': '',
            'bank_name': ['Альфа Банк'],
            'single': True,
            'file_to_bank': dict(),
            'check': False
        },
        'Новоданиловская': {
            'bank_file': r"C:\Users\cyril\Desktop\Самолет\3. Ревью на 30.04.2023г\Новоданиловская 8 +-\Счета ЭСКРОУ_850474049_2023-05-01.xlsx",
            'bank_folder': '',
            'bank_name': ['Дом РФ'],
            'single': True,
            'file_to_bank': dict(),
            'check': False
        },
        'Остафьево': {
            'bank_file': r"C:\Users\cyril\Desktop\Самолет\3. Ревью на 30.04.2023г\Остафьево (СР-Групп) +\CommonDeveloper_01.05.2023_7731319243.xlsx",
            'bank_folder': '',
            'bank_name': ['ВТБ'],
            'single': True,
            'file_to_bank': dict(),
            'check': False
        },
        # 'Путилково': {
        #     'bank_file': '',
        #     'bank_folder': r'C:\Users\cyril\Desktop\Самолет\НОВЫЕ ОТЧЕТЫ\Сверка на 31.03.2023г\Путилково\Выписки"',
        #     'bank_name': ['ГПБ'],
        #     'single': True,
        #     'file_to_bank': {
        #         'Путилково 31.03.23-1.xlsx': (
        #             r"C:\Users\cyril\Desktop\Самолет\НОВЫЕ ОТЧЕТЫ\Сверка на 31.03.2023г\Путилково\Выписки\Путилково 31.03.23-1.xlsx",
        #             'ГПБ'),
        #         'Путилково 31.03.23-2.xlsx': (
        #             r"C:\Users\cyril\Desktop\Самолет\НОВЫЕ ОТЧЕТЫ\Сверка на 31.03.2023г\Путилково\Выписки\Путилково 31.03.23-2.xlsx",
        #             'ГПБ')
        #     },
        #     'check': False
        # },
        'Спутник': {
            'bank_file': '',
            'bank_folder': r'C:\Users\cyril\Desktop\Самолет\3. Ревью на 30.04.2023г\Спутник\Банк',
            'bank_name': '',
            'single': False,
            'file_to_bank': {
                'Отчёт ПСБ.xlsx': (
                    r"C:\Users\cyril\Desktop\Самолет\3. Ревью на 30.04.2023г\Спутник\Банк\Отчёт ПСБ.xlsx",
                    'ПСБ'),
                'отчет эскроу дом рф 02.04.2023.xlsx': (
                    r"C:\Users\cyril\Desktop\Самолет\3. Ревью на 30.04.2023г\Спутник\Банк\отчет эскроу дом рф 02.04.2023.xlsx",
                    'Дом РФ'),
                'отчет эскроу совком 31.03.2023.xlsx': (
                    r"C:\Users\cyril\Desktop\Самолет\3. Ревью на 30.04.2023г\Спутник\Банк\отчет эскроу совком 31.03.2023.xlsx",
                    'Совкомбанк')
            },
            'check': False
        },
        'Новое Внуково': {
            'bank_file': r"C:\Users\cyril\Desktop\Самолет\3. Ревью на 30.04.2023г\Новое Внуково, Санино 1\EscrowBalanceReports_01.04.2023-30.04.2023.XLSX",
            'bank_folder': r'',
            'bank_name': ['СБЕР'],
            'single': True,
            'file_to_bank': dict(),
            'check': False
        },
        'Прибрежный парк': {
            'bank_file': r"C:\Users\cyril\Desktop\Самолет\3. Ревью на 30.04.2023г\Прибрежный парк\EscrowBalanceReports_01.04.2023-01.05.2023.XLSX",
            'bank_folder': r'',
            'bank_name': ['СБЕР'],
            'single': True,
            'file_to_bank': dict(),
            'check': False
        },
        'Пригород Лесное': {
            'bank_file': r"C:\Users\cyril\Desktop\Самолет\3. Ревью на 30.04.2023г\Пригород Лесное\прл 01.04.2023-02.05.2023.XLSX",
            'bank_folder': '',
            'bank_name': ['СБЕР'],
            'single': True,
            'file_to_bank': dict(),
            'check': False
        },
        'Пятницкие кварталы': {
            'bank_file': r"C:\Users\cyril\Desktop\Самолет\3. Ревью на 30.04.2023г\Пятницкие луга (Юрлово)\Юрлово общий отчет  01.04.2023-30.04.2023.XLSX",
            'bank_folder': '',
            'bank_name': ['СБЕР'],
            'single': True,
            'file_to_bank': dict(),
            'check': False
        },
        'Тропарево Парк': {
            'bank_file': r"C:\Users\cyril\Desktop\Самолет\3. Ревью на 30.04.2023г\Тропарёво Парк, Сам-Дудкино\EscrowBalanceReports_01.04.2023-30.04.2023.XLSX",
            'bank_folder': '',
            'bank_name': ['СБЕР'],
            'single': True,
            'file_to_bank': dict(),
            'check': False
        },
        'Сабурово': {
            'bank_file': r"C:\Users\cyril\Desktop\Самолет\3. Ревью на 30.04.2023г\Сабурово-1 +\Копия Отчет эскроу 02.05.23.xlsx",
            'bank_folder': '',
            'bank_name': ['ГПБ'],
            'single': True,
            'file_to_bank': dict(),
            'check': False
        },
        'Долина Яузы': {
            'bank_file': r"C:\Users\cyril\Desktop\Самолет\3. Ревью на 30.04.2023г\Долина Яузы (СЗ Реновация Мытищи) +\ООО СЗ РЕНОВАЦИЯ-МЫТИЩИ 28.04.2023-01.05.2023 .xlsx",
            'bank_folder': '',
            'bank_name': ['Альфа Банк'],
            'single': True,
            'file_to_bank': dict(),
            'check': False
        },

        'Квартал Западный': {
            'bank_file': r"C:\Users\cyril\Desktop\Самолет\3. Ревью на 30.04.2023г\Квартал Западный +\28.04.2023-01.05.2023.xlsx",
            'bank_folder': '',
            'bank_name': ['Альфа Банк'],
            'single': True,
            'file_to_bank': dict(),
            'check': False
        },

        'Новое Видное': {
            'bank_file': r"C:\Users\cyril\Desktop\Самолет\3. Ревью на 30.04.2023г\Новое Видное - Калиновка +\Копия Отчет Калиновка 2904-(2).xlsx",
            'bank_folder': '',
            'bank_name': ['ГПБ'],
            'single': True,
            'file_to_bank': dict(),
            'check': False
        },

    }
    new_new_control_bank_sum_dict = {'Алхимово': 9127391380, 'Верейская': 3044212839, 'Горки Парк': 15770419237,
                        'Долина Яузы': 566659747,
                        'Егорово Парк': 7825507360, 'Заречье': 3916465446, 'Иванкино': 586885243,
                        'Люберцы': 16206970820, 'Молжаниново': 13021383075, 'Мытищи': 20616160245,
                        'Новоданиловская': 7965965717,
                        'Остафьево': 11532488375, 'Новое Внуково': 15499550132,
                        'Прибрежный парк': 20215342064,
                        'Пригород Лесное': 16856582245, 'Пятницкие кварталы': 5991205075,
                        'Спутник': 13108461305, 'Тропарево Парк': 10767356376, 'Томилино': 15427831925,
                        'Сабурово': 206040623.8,'Квартал Западный': 323914389.7, 'Новое Видное':409853223.2
                                    }

    new_new_account_file_dict = \
        {
            'Алхимово': {
                'account': r"C:\Users\cyril\Desktop\Самолет\3. Ревью на 30.04.2023г\Алхимово\Оборотно-сальдовая ведомость по счету 009.СЭ за ... - Апрель 2023 г. ООО  СПЕЦИАЛИЗИРОВАННЫЙ ЗАСТРОЙЩИК  САМОЛЕТ-АЛХИМОВО.xlsx",
                'bank_name': ['СБЕР'],
                'type': True,
                'check_nomenclature': True,
                'check_account': False
            },
            'Томилино': {
                'account': r"C:\Users\cyril\Desktop\Самолет\3. Ревью на 30.04.2023г\Томилино +\Оборотно-сальдовая ведомость по счету 009.СЭ за ... - Апрель 2023 г. ООО  СЗ  САМОЛЕТ-ТОМИЛИНО.xlsx",
                'bank_name': ['ВТБ'],
                'type': True,
                'check_nomenclature': True,
                'check_account': False
            },
            'Верейская': {
                'account': r"C:\Users\cyril\Desktop\Самолет\3. Ревью на 30.04.2023г\Верейская 41 +\Оборотно-сальдовая ведомость по счету 009.СЭ за ... - Апрель 2023 г. АО  СЗ  САМОЛЕТ-ВЕРЕЙСКАЯ.xlsx",
                'bank_name': ['МКБ'],
                'type': True,
                'check_nomenclature': True,
                'check_account': False
            },
            'Горки Парк': {
                'account': r"C:\Users\cyril\Desktop\Самолет\3. Ревью на 30.04.2023г\Горки Парк, Сам-Коробово\Оборотно-сальдовая ведомость по счету 009.СЭ за ... - Апрель 2023 г. ООО  СЗ  САМОЛЕТ-КОРОБОВО.xlsx",
                'bank_name': ['СБЕР'],
                'type': True,
                'check_nomenclature': True,
                'check_account': False

            },
            'Егорово Парк': {
                'account': r"C:\Users\cyril\Desktop\Самолет\3. Ревью на 30.04.2023г\Егорово Парк, Сам-Жилино\Оборотно-сальдовая ведомость по счету 009.СЭ за ... - Апрель 2023 г. ООО  СЗ  САМОЛЕТ-ЖИЛИНО.xlsx",
                'bank_name': ['СБЕР'],
                'type': True,
                'check_nomenclature': True,
                'check_account': False
            },
            'Заречье': {
                'account': r"C:\Users\cyril\Desktop\Самолет\3. Ревью на 30.04.2023г\Заречье +-\Оборотно-сальдовая ведомость по счету 009.СЭ за ... - Апрель 2023 г. ООО  СПЕЦИАЛИЗИРОВАННЫЙ ЗАСТРОЙЩИК  САМОЛЕТ-ЗАРЕЧЬЕ.xlsx",
                'bank_name': ['Совкомбанк'],
                'type': True,
                'check_nomenclature': True,
                'check_account': False
            },
            'Иванкино': {
                'account': r"C:\Users\cyril\Desktop\Самолет\3. Ревью на 30.04.2023г\Квартал Иванкино (Самолёт-Олимп) +\Оборотно-сальдовая ведомость по счету 009.СЭ за ... - Апрель 2023 г. ООО  СЗ  САМОЛЕТ-ОЛИМП.xlsx",
                'bank_name': ['МКБ'],
                'type': True,
                'check_nomenclature': True,
                'check_account': False
            },
            # 'Лайково': {
            #     'account': r"C:\Users\cyril\Desktop\Самолет\НОВЫЕ ОТЧЕТЫ\Сверка на 31.03.2023г\Лайково\Оборотно-сальдовая ведомость по счету 009.СЭ САМОЛЕТ-ЛАЙКОВО.xlsx",
            #     'bank_name': ['Дом РФ'],
            #     'type': True,
            #     'check_nomenclature': True,
            #     'check_account': False
            # },
            'Люберцы': {
                'account': r"C:\Users\cyril\Desktop\Самолет\3. Ревью на 30.04.2023г\Люберцы +\Оборотно-сальдовая ведомость по счету 009.СЭ за ... - Апрель 2023 г. ООО  СЗ  САМОЛЕТ ДЕВЕЛОПМЕНТ.xlsx",
                'bank_name': ['Альфа Банк'],
                'type': True,
                'check_nomenclature': True,
                'check_account': False

            },
            'Молжаниново': {
                'account': r"C:\Users\cyril\Desktop\Самолет\3. Ревью на 30.04.2023г\Молжаниново +\Оборотно-сальдовая ведомость по счету 009.СЭ за ... - Апрель 2023 г. ООО  СПЕЦИАЛИЗИРОВАННЫЙ ЗАСТРОЙЩИК  САМОЛЕТ-МОЛЖАНИНОВО.xlsx",
                'bank_name': ['МКБ'],
                'type': True,
                'check_nomenclature': True,
                'check_account': False
            },
            'Мытищи': {
                'account': r"C:\Users\cyril\Desktop\Самолет\3. Ревью на 30.04.2023г\Мытищи Парк (Самолет-Мытищи) +\ОСВ по счету 009.СЭ за ... - Апрель 2023 г. ООО  СПЕЦИАЛИЗИРОВАННЫЙ ЗАСТРОЙЩИК  САМОЛЕТ-МЫТИЩИ.xlsx",
                'bank_name': ['Альфа Банк'],
                'type': True,
                'check_nomenclature': True,
                'check_account': False
            },
            'Новоданиловская': {
                'account': r"C:\Users\cyril\Desktop\Самолет\3. Ревью на 30.04.2023г\Новоданиловская 8 +-\Оборотно-сальдовая ведомость по счету 009.СЭ за ... - Апрель 2023 г. ООО  СПЕЦИАЛИЗИРОВАННЫЙ ЗАСТРОЙЩИК  ДМ АПАРТМЕНТС.xlsx",
                'bank_name': ['Дом РФ'],
                'type': True,
                'check_nomenclature': True,
                'check_account': False
            },
            'Остафьево': {
                'account': r"C:\Users\cyril\Desktop\Самолет\3. Ревью на 30.04.2023г\Остафьево (СР-Групп) +\Оборотно-сальдовая ведомость по счету 009.СЭ за ... - Апрель 2023 г. ООО  СПЕЦИАЛИЗИРОВАННЫЙ ЗАСТРОЙЩИК  СР-ГРУПП.xlsx",
                'bank_name': ['ВТБ'],
                'type': True,
                'check_nomenclature': True,
                'check_account': False
            },
            'Путилково': {
                'account': r"C:\Users\cyril\Desktop\Самолет\3. Ревью на 30.04.2023г\Большое Путилково +\Оборотно-сальдовая ведомость по счету 009.СЭ за ... - Апрель 2023 г. ООО  СЗ  САМОЛЕТ-ПУТИЛКОВО.xlsx",
                'bank_name': ['ГПБ'],
                'type': True,
                'check_nomenclature': True,
                'check_account': False
            },
            'Новое Внуково': {
                'account': r"C:\Users\cyril\Desktop\Самолет\3. Ревью на 30.04.2023г\Новое Внуково, Санино 1\Оборотно-сальдовая ведомость по счету 009.СЭ за ... - Апрель 2023 г. ООО  СЗ  САНИНО 1.xlsx",
                'bank_name': ['СБЕР'],
                'type': True,
                'check_nomenclature': True,
                'check_account': False
            },
            'Прибрежный парк': {
                'account': r"C:\Users\cyril\Desktop\Самолет\3. Ревью на 30.04.2023г\Прибрежный парк\Оборотно-сальдовая ведомость по счету 009.СЭ за ... - Апрель 2023 г. ООО  СЗ  ПРИБРЕЖНЫЙ ПАРК.xlsx",
                'bank_name': ['СБЕР'],
                'type': True,
                'check_nomenclature': True,
                'check_account': False
            },
            'Пригород Лесное': {
                'account': r"C:\Users\cyril\Desktop\Самолет\3. Ревью на 30.04.2023г\Пригород Лесное\Оборотно-сальдовая ведомость по счету 009.СЭ за ... - Апрель 2023 г. ООО  СЗ  ПРИГОРОД ЛЕСНОЕ.xlsx",
                'bank_name': ['СБЕР'],
                'type': True,
                'check_nomenclature': True,
                'check_account': False
            },
            'Пятницкие кварталы': {
                'account': r"C:\Users\cyril\Desktop\Самолет\3. Ревью на 30.04.2023г\Пятницкие луга (Юрлово)\Оборотно-сальдовая ведомость по счету 009.СЭ за ... - Апрель 2023 г. ООО  СЗ  САМОЛЕТ-ЮРЛОВО.xlsx",
                'bank_name': ['СБЕР'],
                'type': True,
                'check_nomenclature': True,
                'check_account': False
            },
            'Спутник': {
                'account': r"C:\Users\cyril\Desktop\Самолет\3. Ревью на 30.04.2023г\Спутник\Оборотно-сальдовая ведомость по счету 009.СЭ за ... - Апрель 2023 г. ООО  СЗ  БУХТА ЛЭНД.xlsx",
                'bank_name': ['ПСБ'],
                'type': True,
                'check_nomenclature': True,
                'check_account': False
            },
            'Тропарево Парк': {
                'account': r"C:\Users\cyril\Desktop\Самолет\3. Ревью на 30.04.2023г\Тропарёво Парк, Сам-Дудкино\Оборотно-сальдовая ведомость по счету 009.СЭ за ... - Апрель 2023 г. ООО  СЗ  САМОЛЕТ-ДУДКИНО.xlsx",
                'bank_name': ['СБЕР'],
                'type': True,
                'check_nomenclature': True,
                'check_account': False
            },
            'Сабурово': {
                'account': r"C:\Users\cyril\Desktop\Самолет\3. Ревью на 30.04.2023г\Сабурово-1 +\Оборотно-сальдовая ведомость по счету 009.СЭ за ... - Апрель 2023 г. ООО  СЗ  САМОЛЕТ-САБУРОВО-1.xlsx",
                'bank_name': ['ГПБ'],
                'type': True,
                'check_nomenclature': True,
                'check_account': False
            },
            'Долина Яузы': {
                'account': r"C:\Users\cyril\Desktop\Самолет\3. Ревью на 30.04.2023г\Долина Яузы (СЗ Реновация Мытищи) +\Оборотно-сальдовая ведомость по счету 009.СЭ за ... - Апрель 2023 г. ООО  СЗ  РЕНОВАЦИЯ-МЫТИЩИ.xlsx",
                'bank_name': ['Альфа Банк'],
                'type': True,
                'check_nomenclature': True,
                'check_account': False
            },
            'Квартал Западный': {
                'account': r"C:\Users\cyril\Desktop\Самолет\3. Ревью на 30.04.2023г\Квартал Западный +\Оборотно-сальдовая ведомость по счету 009.СЭ за ... - Апрель 2023 г. ООО  СЗ  САМОЛЕТ-КВАРТАЛ ЗАПАДНЫЙ.xlsx",
                'bank_name': ['Альфа Банк'],
                'type': True,
                'check_nomenclature': True,
                'check_account': False
            },
            'Новое Видное': {
                'account': r"C:\Users\cyril\Desktop\Самолет\3. Ревью на 30.04.2023г\Новое Видное - Калиновка +\Оборотно-сальдовая ведомость по счету 009.СЭ за ... - Апрель 2023 г. ООО  СЗ  САМОЛЕТ-КАЛИНОВКА.xlsx",
                'bank_name': ['ГПБ'],
                'type': True,
                'check_nomenclature': True,
                'check_account': False
            }
        }


    new_new_control_account_sum_dict = {'Алхимово': 9293268224.90, 'Верейская': 2606392710.35, 'Горки Парк': 15770419237.49,
                            'Долина Яузы': 566659747.29,
                            'Егорово Парк': 7825507360.25, 'Заречье': 7471434735.75, 'Иванкино': 586885243.11,
                            'Люберцы': 16203119479.74, 'Молжаниново': 13016865517.25, 'Мытищи': 20631435384.17,
                            'Новоданиловская': 7965965716.86,
                            'Остафьево': 11532488374.59, 'Путилково': 11347555216.59, 'Новое Внуково': 15499550131.77,
                            'Прибрежный парк': 20215362063.75,
                            'Пригород Лесное': 3080655346, 'Пятницкие кварталы': 5991205075.03,
                            'Спутник': 13988397306.58, 'Тропарево Парк': 10767356353.62, 'Томилино': 15234802248.21,
                            'Сабурово': 206040623.75, 'Квартал Западный': 323914389.74, 'Новое Видное': 409853223.2}



    def test_new_new_bank(self):
        for key, value in self.new_new_bank_file_dict.items():
            account = AccountFile(self.new_new_account_file_dict[key])
            print(key)
            bank = BankFile(value, account.type_dict)
            number = bank.document_sum
            self.assertEqual(round(number), round(self.new_new_control_bank_sum_dict[key]))
    #

    def test_new_new_account(self):
        for key, value in self.new_new_account_file_dict.items():
            number = AccountFile(value).document_sum
            self.assertEqual(round(number), round(self.new_new_control_account_sum_dict[key]))