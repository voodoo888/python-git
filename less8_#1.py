class Date:
    def __init__(self, input_date):
        self.input_date = input_date

    @classmethod
    def method_integer(cls, date):
        result = [int(i) for i in date.input_date.split('-')]
        return result

    @staticmethod
    def valid_method(day, month, year):
        invalid = 'Невалидное значение'
        valid = 'Ошибок ввода не найдено'
        result = []
        if 0 < day <= 31:
            result.append(valid)
        else:
            result.append(invalid)
        if 0 < month <= 12:
            result.append(valid)
        else:
            result.append(invalid)
        if 2000 < year <= 2022:
            result.append(valid)
        else:
            result.append(invalid)
        return print(result)


f = Date('32-12-2021')
extract = Date.method_integer(f)
print(extract)
day, month, year = extract
print(day, month, year)
f.valid_method(day, month, year)
