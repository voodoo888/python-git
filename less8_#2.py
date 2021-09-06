class ZeroError(Exception):
    def __init__(self, text):
        self.text = text


num1 = float(input('Введите число 1: '))
try:
    num2 = float(input('Введите число 2: '))
    if num2 == 0:
        raise ZeroError('На ноль делить нельзя')
except ZeroError as err:
    print(err)
else:
    result = num1 / num2
    print(result)
finally:
    print('END')
