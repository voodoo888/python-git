def division():
    """ Возвращает результат деления двух введенных чисел"""
    arg1 = int(input('Введите число 1: '))
    arg2 = int(input('Введите число 2: '))
    try:
        result = arg1/arg2
    except ZeroDivisionError:
        result = 'Деление на 0 невозможно!'
    return result


print(division())
