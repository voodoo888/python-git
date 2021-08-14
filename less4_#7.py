# факториал
from math import factorial


def fact(n):
    """Возвращает генератор содержащий факториалы от 1 до n"""
    for i in range(1, n+1):
        yield factorial(i)


for el in fact(6):
    print(el)