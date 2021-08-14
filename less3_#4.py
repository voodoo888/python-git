# Программа возведения X в отрицательную степень Y

x = int(input('Введите действительное положительное число X: '))
y = int(input('Введите  отрицательное целое число Y: '))


def my_func(x, y):
    """Возвращает результат возведения числа X в степень Y"""
    return x ** y


def my_func1(x, y):
    """Возвращает результат возведения числа X в степень Y """
    result = 1
    while y < 0:
        y = y + 1
        result = result * x
    return 1 / result


print(my_func(x, y))
print(my_func1(x, y))
