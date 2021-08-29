class DigitError(Exception):
    def __init__(self, text):
        self.text = text


num = 0
result = []
while num != 'stop':
    try:
        num = input('Введите число или "stop": ')
        if num == 'stop':
            continue
        for el in num:
            if el.isdigit():
                valid = True
            else:
                valid = False
                raise DigitError('Is not number')
        if valid is True:
            result.append(num)
    except DigitError as err:
        print(err)
print(result)
