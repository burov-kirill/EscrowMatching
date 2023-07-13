################################################################################################
import unittest

from settings.classes.account import AccountFile


class TestCalc(unittest.TestCase):
    new_bank_file_dict = {
        'Алхимово': {
            'bank_file': r"W:\ФИНАНСОВО-ПРАВОВОЙ БЛОК\Дирекция по экономике и финансам\МСФО\Сверка Эскроу\Для тестов\2. Сверка на 31.03.2023г\Алхимово (R)+\Алхимово общий отчет-01.03.2023-31.03.2023.xlsx",
            'bank_folder': '',
            'bank_name': ['СБЕР'],
            'single': True,
            'file_to_bank': dict(),
            'check': False
        },
        'Томилино': {
            'bank_file': r"W:\ФИНАНСОВО-ПРАВОВОЙ БЛОК\Дирекция по экономике и финансам\МСФО\Сверка Эскроу\Для тестов\2. Сверка на 31.03.2023г\Томилино (R)\CommonDeveloper_01.04.2023_5027240182.xlsx",
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
            'bank_file': r"W:\ФИНАНСОВО-ПРАВОВОЙ БЛОК\Дирекция по экономике и финансам\МСФО\Сверка Эскроу\Для тестов\2. Сверка на 31.03.2023г\Горки Парк, Сам-Коробово (R)+\Отчёт 31.03.2023.xlsx",
            'bank_folder': '',
            'bank_name': ['СБЕР'],
            'single': True,
            'file_to_bank': dict(),
            'check': False
        },
        'Егорово Парк': {
            'bank_file': r"W:\ФИНАНСОВО-ПРАВОВОЙ БЛОК\Дирекция по экономике и финансам\МСФО\Сверка Эскроу\Для тестов\2. Сверка на 31.03.2023г\Егорово Парк, Сам-Жилино (R)+\EscrowBalanceReports_01.03.2023-31.03.2023.xlsx",
            'bank_folder': r'',
            'bank_name': ['СБЕР'],
            'single': True,
            'file_to_bank': dict(),
            'check': False
        },
        'Заречье': {
            'bank_file': r"W:\ФИНАНСОВО-ПРАВОВОЙ БЛОК\Дирекция по экономике и финансам\МСФО\Сверка Эскроу\Для тестов\2. Сверка на 31.03.2023г\Заречье (R)\Банк\ООО СЗ Самолет-Заречье 01.01.2019 - 31.03.2023.xlsx",
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
        # 'Лайково': {
        #     'bank_file': r"C:\Users\cyril\Desktop\Самолет\НОВЫЕ ОТЧЕТЫ\Сверка на 31.03.2023г\Лайково\Выписки\Счета ЭСКРОУ_1043532145_2023-03-31.xlsx",
        #     'bank_folder': '',
        #     'bank_name': ['Дом РФ'],
        #     'single': True,
        #     'file_to_bank': dict(),
        #     'check': False
        # },
        'Люберцы': {
            'bank_file': r"W:\ФИНАНСОВО-ПРАВОВОЙ БЛОК\Дирекция по экономике и финансам\МСФО\Сверка Эскроу\Для тестов\2. Сверка на 31.03.2023г\Люберцы (R)\Люб месяц.XLSX",
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
            'bank_file': r"W:\ФИНАНСОВО-ПРАВОВОЙ БЛОК\Дирекция по экономике и финансам\МСФО\Сверка Эскроу\Для тестов\2. Сверка на 31.03.2023г\Мытищи Парк (Самолет-Мытищи) (R)+\МЫТИЩИ месяц.XLSX",
            'bank_folder': '',
            'bank_name': ['Альфа Банк'],
            'single': True,
            'file_to_bank': dict(),
            'check': False
        },
        'Новоданиловская': {
            'bank_file': r"W:\ФИНАНСОВО-ПРАВОВОЙ БЛОК\Дирекция по экономике и финансам\МСФО\Сверка Эскроу\Для тестов\2. Сверка на 31.03.2023г\Новоданиловская 8 (R)\Счета ЭСКРОУ_850474049_2023-03-31.xlsx",
            'bank_folder': '',
            'bank_name': ['Дом РФ'],
            'single': True,
            'file_to_bank': dict(),
            'check': False
        },
        'Остафьево': {
            'bank_file': r"W:\ФИНАНСОВО-ПРАВОВОЙ БЛОК\Дирекция по экономике и финансам\МСФО\Сверка Эскроу\Для тестов\2. Сверка на 31.03.2023г\Остафьево (СР-Групп) (R)+\CommonDeveloper_01.04.2023_7731319243.xlsx",
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
            'bank_folder': r'W:\ФИНАНСОВО-ПРАВОВОЙ БЛОК\Дирекция по экономике и финансам\МСФО\Сверка Эскроу\Для тестов\2. Сверка на 31.03.2023г\Спутник\Банк',
            'bank_name': '',
            'single': False,
            'file_to_bank': {
                'отчет эскроу дом рф 02.04.2023.xlsx': (
                    r"W:\ФИНАНСОВО-ПРАВОВОЙ БЛОК\Дирекция по экономике и финансам\МСФО\Сверка Эскроу\Для тестов\2. Сверка на 31.03.2023г\Спутник\Банк\отчет эскроу дом рф 02.04.2023.xlsx",
                    'Дом РФ'),
                'отчет эскроу совком 31.03.2023.xlsx': (
                    r"W:\ФИНАНСОВО-ПРАВОВОЙ БЛОК\Дирекция по экономике и финансам\МСФО\Сверка Эскроу\Для тестов\2. Сверка на 31.03.2023г\Спутник\Банк\отчет эскроу совком 31.03.2023.xlsx",
                    'Совкомбанк')
            },
            'check': False
        },
        'Новое Внуково': {
            'bank_file': r"W:\ФИНАНСОВО-ПРАВОВОЙ БЛОК\Дирекция по экономике и финансам\МСФО\Сверка Эскроу\Для тестов\2. Сверка на 31.03.2023г\Новое Внуково, Санино 1 (R)+\EscrowBalanceReports_01.03.2023-31.03.2023.xlsx",
            'bank_folder': r'',
            'bank_name': ['СБЕР'],
            'single': True,
            'file_to_bank': dict(),
            'check': False
        },
        'Прибрежный парк': {
            'bank_file': r"W:\ФИНАНСОВО-ПРАВОВОЙ БЛОК\Дирекция по экономике и финансам\МСФО\Сверка Эскроу\Для тестов\2. Сверка на 31.03.2023г\Прибрежный парк (R)+\EscrowBalanceReports_01.03.2023-31.03.2023.xlsx",
            'bank_folder': r'',
            'bank_name': ['СБЕР'],
            'single': True,
            'file_to_bank': dict(),
            'check': False
        },
        'Пригород Лесное': {
            'bank_file': r"W:\ФИНАНСОВО-ПРАВОВОЙ БЛОК\Дирекция по экономике и финансам\МСФО\Сверка Эскроу\Для тестов\2. Сверка на 31.03.2023г\Пригород Лесное  (R)+\EscrowBalanceReports_01.03.2023-31.03.2023.xlsx",
            'bank_folder': '',
            'bank_name': ['СБЕР'],
            'single': True,
            'file_to_bank': dict(),
            'check': False
        },
        'Пятницкие кварталы': {
            'bank_file': r"W:\ФИНАНСОВО-ПРАВОВОЙ БЛОК\Дирекция по экономике и финансам\МСФО\Сверка Эскроу\Для тестов\2. Сверка на 31.03.2023г\Пятницкие луга (Юрлово) (R)+\Юрлово общий отчет-01.03.2023-31.03.2023.xlsx",
            'bank_folder': '',
            'bank_name': ['СБЕР'],
            'single': True,
            'file_to_bank': dict(),
            'check': False
        },
        'Тропарево Парк': {
            'bank_file': r"W:\ФИНАНСОВО-ПРАВОВОЙ БЛОК\Дирекция по экономике и финансам\МСФО\Сверка Эскроу\Для тестов\2. Сверка на 31.03.2023г\Тропарёво Парк, Сам-Дудкино (R)+\EscrowBalanceReports_01.03.2023-31.03.2023.xlsx",
            'bank_folder': '',
            'bank_name': ['СБЕР'],
            'single': True,
            'file_to_bank': dict(),
            'check': False
        },
        'Сабурово': {
            'bank_file': r"W:\ФИНАНСОВО-ПРАВОВОЙ БЛОК\Дирекция по экономике и финансам\МСФО\Сверка Эскроу\Для тестов\2. Сверка на 31.03.2023г\Сабурово-1 (Р)\Отчет эскроу 31.03.23.xlsx",
            'bank_folder': '',
            'bank_name': ['ГПБ'],
            'single': True,
            'file_to_bank': dict(),
            'check': False
        },
        'Долина Яузы': {
            'bank_file': r"W:\ФИНАНСОВО-ПРАВОВОЙ БЛОК\Дирекция по экономике и финансам\МСФО\Сверка Эскроу\Для тестов\2. Сверка на 31.03.2023г\Долина Яузы (СЗ Реновация Мытищи) (R)\РМ месяц.XLSX",
            'bank_folder': '',
            'bank_name': ['Альфа Банк'],
            'single': True,
            'file_to_bank': dict(),
            'check': False
        },

        'Квартал Западный': {
            'bank_file': r"W:\ФИНАНСОВО-ПРАВОВОЙ БЛОК\Дирекция по экономике и финансам\МСФО\Сверка Эскроу\Для тестов\2. Сверка на 31.03.2023г\Квартал Западный (R)\КЗ месяц.XLSX",
            'bank_folder': '',
            'bank_name': ['Альфа Банк'],
            'single': True,
            'file_to_bank': dict(),
            'check': False
        },

        'Новое Видное': {
            'bank_file': '',
            'bank_folder': r'W:\ФИНАНСОВО-ПРАВОВОЙ БЛОК\Дирекция по экономике и финансам\МСФО\Сверка Эскроу\Для тестов\2. Сверка на 31.03.2023г\Новое Видное - Калиновка (Р)\Выпсики',
            'bank_name': '',
            'single': True,
            'file_to_bank': {
                'Отчет Калиновка 0104-(1).xlsx': (
                    r"W:\ФИНАНСОВО-ПРАВОВОЙ БЛОК\Дирекция по экономике и финансам\МСФО\Сверка Эскроу\Для тестов\2. Сверка на 31.03.2023г\Новое Видное - Калиновка (Р)\Выпсики\Отчет Калиновка 0104-(1).xlsx",
                    'ГПБ'),
                'Отчет Калиновка 0104-(2).xlsx': (
                    r"W:\ФИНАНСОВО-ПРАВОВОЙ БЛОК\Дирекция по экономике и финансам\МСФО\Сверка Эскроу\Для тестов\2. Сверка на 31.03.2023г\Новое Видное - Калиновка (Р)\Выпсики\Отчет Калиновка 0104-(2).xlsx",
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
                                 'Пятницкие кварталы': 5636631196.88, 'Тропарево Парк': 10428259337.10,
                                 'Томилино': 19274389667.30,
                                 'Сабурово': 132014609, 'Квартал Западный': 206050296.7, 'Новое Видное': 576420296
                                 }
    new_account_file_dict = \
        {
            'Алхимово': {
                'account': r"W:\ФИНАНСОВО-ПРАВОВОЙ БЛОК\Дирекция по экономике и финансам\МСФО\Сверка Эскроу\Для тестов\2. Сверка на 31.03.2023г\Алхимово (R)+\ОСВ по счету 009.СЭ за ... - 1 квартал 2023 г.АЛХИМОВО.xlsx",
                'bank_name': ['СБЕР'],
                'type': True,
                'check_nomenclature': True,
                'check_account': False
            },
            'Томилино': {
                'account': r"W:\ФИНАНСОВО-ПРАВОВОЙ БЛОК\Дирекция по экономике и финансам\МСФО\Сверка Эскроу\Для тестов\2. Сверка на 31.03.2023г\Томилино (R)\Оборотно-сальдовая ведомость по счету 009.СЭ САМОЛЕТ-ТОМИЛИНО.xlsx",
                'bank_name': ['ВТБ'],
                'type': True,
                'check_nomenclature': True,
                'check_account': False
            },
            'Верейская': {
                'account': r"W:\ФИНАНСОВО-ПРАВОВОЙ БЛОК\Дирекция по экономике и финансам\МСФО\Сверка Эскроу\Для тестов\2. Сверка на 31.03.2023г\Верейская 41 (R)\Оборотно-сальдовая ведомость по счету 009.СЭ  СЗ  САМОЛЕТ-ВЕРЕЙСКАЯ.xlsx",
                'bank_name': ['МКБ'],
                'type': True,
                'check_nomenclature': True,
                'check_account': False
            },
            'Горки Парк': {
                'account': r"W:\ФИНАНСОВО-ПРАВОВОЙ БЛОК\Дирекция по экономике и финансам\МСФО\Сверка Эскроу\Для тестов\2. Сверка на 31.03.2023г\Горки Парк, Сам-Коробово (R)+\ОСВ по счету 009.СЭ СЗ  САМОЛЕТ-КОРОБОВО.xlsx",
                'bank_name': ['СБЕР'],
                'type': True,
                'check_nomenclature': True,
                'check_account': False

            },
            'Егорово Парк': {
                'account': r"W:\ФИНАНСОВО-ПРАВОВОЙ БЛОК\Дирекция по экономике и финансам\МСФО\Сверка Эскроу\Для тестов\2. Сверка на 31.03.2023г\Егорово Парк, Сам-Жилино (R)+\ОСВ по счету 009.СЭ СЗ  САМОЛЕТ-ЖИЛИНО.xlsx",
                'bank_name': ['СБЕР'],
                'type': True,
                'check_nomenclature': True,
                'check_account': False
            },
            'Заречье': {
                'account': r"W:\ФИНАНСОВО-ПРАВОВОЙ БЛОК\Дирекция по экономике и финансам\МСФО\Сверка Эскроу\Для тестов\2. Сверка на 31.03.2023г\Заречье (R)\Оборотно-сальдовая ведомость по счету 009.СЭ САМОЛЕТ-ЗАРЕЧЬЕ.xlsx",
                'bank_name': ['Совкомбанк'],
                'type': True,
                'check_nomenclature': True,
                'check_account': False
            },
            'Иванкино': {
                'account': r"W:\ФИНАНСОВО-ПРАВОВОЙ БЛОК\Дирекция по экономике и финансам\МСФО\Сверка Эскроу\Для тестов\2. Сверка на 31.03.2023г\Квартал Иванкино (Самолёт-Олимп) (R)\ОСВ по счету 009.СЭ САМОЛЕТ-ОЛИМП.xlsx",
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
                'account': r"W:\ФИНАНСОВО-ПРАВОВОЙ БЛОК\Дирекция по экономике и финансам\МСФО\Сверка Эскроу\Для тестов\2. Сверка на 31.03.2023г\Люберцы (R)\Оборотно-сальдовая ведомость по счету 009.СЭ САМОЛЕТ ДЕВЕЛОПМЕНТ.xlsx",
                'bank_name': ['Альфа Банк'],
                'type': True,
                'check_nomenclature': True,
                'check_account': False

            },
            'Молжаниново': {
                'account': r"W:\ФИНАНСОВО-ПРАВОВОЙ БЛОК\Дирекция по экономике и финансам\МСФО\Сверка Эскроу\Для тестов\2. Сверка на 31.03.2023г\Молжаниново (R)\Оборотно-сальдовая ведомость по счету 009.СЭ САМОЛЕТ-МОЛЖАНИНОВО.xlsx",
                'bank_name': ['МКБ'],
                'type': True,
                'check_nomenclature': True,
                'check_account': False
            },
            'Мытищи': {
                'account': r"W:\ФИНАНСОВО-ПРАВОВОЙ БЛОК\Дирекция по экономике и финансам\МСФО\Сверка Эскроу\Для тестов\2. Сверка на 31.03.2023г\Мытищи Парк (Самолет-Мытищи) (R)+\Оборотно-сальдовая ведомость по счету 009.СЭ САМОЛЕТ-МЫТИЩИ.xlsx",
                'bank_name': ['Альфа Банк'],
                'type': True,
                'check_nomenclature': True,
                'check_account': False
            },
            'Новоданиловская': {
                'account': r"W:\ФИНАНСОВО-ПРАВОВОЙ БЛОК\Дирекция по экономике и финансам\МСФО\Сверка Эскроу\Для тестов\2. Сверка на 31.03.2023г\Новоданиловская 8 (R)\Оборотно-сальдовая ведомость по счету 009.СЭ ДМ АПАРТМЕНТС.xlsx",
                'bank_name': ['Дом РФ'],
                'type': True,
                'check_nomenclature': True,
                'check_account': False
            },
            'Остафьево': {
                'account': r"W:\ФИНАНСОВО-ПРАВОВОЙ БЛОК\Дирекция по экономике и финансам\МСФО\Сверка Эскроу\Для тестов\2. Сверка на 31.03.2023г\Остафьево (СР-Групп) (R)+\Оборотно-сальдовая ведомость по счету 009.СЭ СР-ГРУПП.xlsx",
                'bank_name': ['ВТБ'],
                'type': True,
                'check_nomenclature': True,
                'check_account': False
            },
            # 'Путилково': {
            #     'account': r"C:\Users\cyril\Desktop\Самолет\НОВЫЕ ОТЧЕТЫ\Сверка на 31.03.2023г\Путилково\Оборотно-сальдовая ведомость по счету 009.СЭ САМОЛЕТ-ПУТИЛКОВО.xlsx",
            #     'bank_name': ['ГПБ'],
            #     'type': True,
            #     'check_nomenclature': True,
            #     'check_account': False
            # },
            'Новое Внуково': {
                'account': r"W:\ФИНАНСОВО-ПРАВОВОЙ БЛОК\Дирекция по экономике и финансам\МСФО\Сверка Эскроу\Для тестов\2. Сверка на 31.03.2023г\Новое Внуково, Санино 1 (R)+\Оборотно-сальдовая ведомость по счету 009.СЭ СЗ  САНИНО 1.xlsx",
                'bank_name': ['СБЕР'],
                'type': True,
                'check_nomenclature': True,
                'check_account': False
            },
            'Прибрежный парк': {
                'account': r"W:\ФИНАНСОВО-ПРАВОВОЙ БЛОК\Дирекция по экономике и финансам\МСФО\Сверка Эскроу\Для тестов\2. Сверка на 31.03.2023г\Прибрежный парк (R)+\ОСВ по счету 009.СЭ СЗ  ПРИБРЕЖНЫЙ ПАРК.xlsx",
                'bank_name': ['СБЕР'],
                'type': True,
                'check_nomenclature': True,
                'check_account': False
            },
            'Пригород Лесное': {
                'account': r"W:\ФИНАНСОВО-ПРАВОВОЙ БЛОК\Дирекция по экономике и финансам\МСФО\Сверка Эскроу\Для тестов\2. Сверка на 31.03.2023г\Пригород Лесное  (R)+\Оборотно-сальдовая ведомость по счету 009.СЭ ПРИГОРОД ЛЕСНОЕ.xlsx",
                'bank_name': ['СБЕР'],
                'type': True,
                'check_nomenclature': True,
                'check_account': False
            },
            'Пятницкие кварталы': {
                'account': r"W:\ФИНАНСОВО-ПРАВОВОЙ БЛОК\Дирекция по экономике и финансам\МСФО\Сверка Эскроу\Для тестов\2. Сверка на 31.03.2023г\Пятницкие луга (Юрлово) (R)+\ОСВ по счету 009.СЭ САМОЛЕТ-ЮРЛОВО.xlsx",
                'bank_name': ['СБЕР'],
                'type': True,
                'check_nomenclature': True,
                'check_account': False
            },
            'Спутник': {
                'account': r"W:\ФИНАНСОВО-ПРАВОВОЙ БЛОК\Дирекция по экономике и финансам\МСФО\Сверка Эскроу\Для тестов\2. Сверка на 31.03.2023г\Спутник\Оборотно-сальдовая ведомость по счету 009.СЭ СЗ  БУХТА ЛЭНД.xlsx",
                'bank_name': ['ПСБ'],
                'type': True,
                'check_nomenclature': True,
                'check_account': False
            },
            'Тропарево Парк': {
                'account': r"W:\ФИНАНСОВО-ПРАВОВОЙ БЛОК\Дирекция по экономике и финансам\МСФО\Сверка Эскроу\Для тестов\2. Сверка на 31.03.2023г\Тропарёво Парк, Сам-Дудкино (R)+\Оборотно-сальдовая ведомость по счету 009.СЭ САМОЛЕТ-ДУДКИНО.xlsx",
                'bank_name': ['СБЕР'],
                'type': True,
                'check_nomenclature': True,
                'check_account': False
            },
            'Сабурово': {
                'account': r"W:\ФИНАНСОВО-ПРАВОВОЙ БЛОК\Дирекция по экономике и финансам\МСФО\Сверка Эскроу\Для тестов\2. Сверка на 31.03.2023г\Сабурово-1 (Р)\Оборотно-сальдовая ведомость по счету 009.СЭ САМОЛЕТ-САБУРОВО-1.xlsx",
                'bank_name': ['ГПБ'],
                'type': True,
                'check_nomenclature': True,
                'check_account': False
            },
            'Долина Яузы': {
                'account': r"W:\ФИНАНСОВО-ПРАВОВОЙ БЛОК\Дирекция по экономике и финансам\МСФО\Сверка Эскроу\Для тестов\2. Сверка на 31.03.2023г\Долина Яузы (СЗ Реновация Мытищи) (R)\Оборотно-сальдовая ведомость по счету 009.СЭ СЗ  РЕНОВАЦИЯ-МЫТИЩИ.xlsx",
                'bank_name': ['Альфа Банк'],
                'type': True,
                'check_nomenclature': True,
                'check_account': False
            },
            'Квартал Западный': {
                'account': r"W:\ФИНАНСОВО-ПРАВОВОЙ БЛОК\Дирекция по экономике и финансам\МСФО\Сверка Эскроу\Для тестов\2. Сверка на 31.03.2023г\Квартал Западный (R)\Оборотно-сальдовая ведомость по счету 009.СЭ САМОЛЕТ-КВАРТАЛ ЗАПАДНЫЙ.xlsx",
                'bank_name': ['Альфа Банк'],
                'type': True,
                'check_nomenclature': True,
                'check_account': False
            },
            'Новое Видное': {
                'account': r"W:\ФИНАНСОВО-ПРАВОВОЙ БЛОК\Дирекция по экономике и финансам\МСФО\Сверка Эскроу\Для тестов\2. Сверка на 31.03.2023г\Новое Видное - Калиновка (Р)\Оборотно-сальдовая ведомость по счету 009.СЭ САМОЛЕТ-КАЛИНОВКА.xlsx",
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
                                    'Остафьево': 10560598756.83, 'Путилково': 11013151651.59,
                                    'Новое Внуково': 14661311482.92,
                                    'Прибрежный парк': 19280212387.45,
                                    'Пригород Лесное': 30243644354.83, 'Пятницкие кварталы': 5637486491.07,
                                    'Спутник': 13119588751.36, 'Тропарево Парк': 10429392326.14, 'Томилино': 19081309990.91,
                                    'Сабурово': 132014608.58, 'Квартал Западный': 206050296.73, 'Новое Видное': 288210147.84
                                    }


    # def test_new_bank(self):
    #     for key, value in self.new_bank_file_dict.items():
    #         account = AccountFile(self.new_account_file_dict[key])
    #         print(key)
    #         bank = BankFile(value, account.type_dict)
    #         number = bank.document_sum
    #         self.assertEqual(round(number), round(self.new_control_bank_sum_dict[key]))


    #

    def test_new_account(self):
        for key, value in self.new_account_file_dict.items():
            number = AccountFile(value).document_sum
            self.assertEqual(round(number), round(self.new_control_account_sum_dict[key]))