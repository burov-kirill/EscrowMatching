
class PatternColumnsError(Exception):
    def __init__(self, pattern, account_columns, message="Нет подходящего паттерна"):
        self.pattern = pattern
        self.account_columns = account_columns
        self.message = message
        super().__init__(self.message)

    def __str__(self):
        return f'{self.pattern} != {self.account_columns}'

class DifferentLengthError(Exception):
    def __init__(self, message="Не соответствует длина фрейма проектов и ОСВ"):

        self.message = message
        super().__init__(self.message)

    def __str__(self):
        return f'{self.message}'


class UserSelectError(Exception):
    def __init__(self, message):
        self.message = message
        super().__init__(self.message)

    def __str__(self):
        return f'{self.message}'

class WorkbookFilterError(ValueError):
    def __init__(self, path, message = ''):
        self.path = path
        self.message = f'Возможно в данной книге {path} открыты фильтры'
        super().__init__(self.message)

    def __str__(self):
        return f'{self.message}'

class NotFoundColumns(KeyError):
    def __init__(self, message = 'Не найдены подходящие столбцы'):
        self.message = message
        super().__init__(self.message)

    def __str__(self):
        return f'{self.message}'

class InterruptScript(Exception):
    def __init__(self, message='Досрочное завершение'):
        self.message = message
        super().__init__(self.message)

    def __str__(self):
        return f'{self.message}'