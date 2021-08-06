# Part1__Генератор целых чисел начиная с указанного
from itertools import count, cycle


def whole_numbers(x, y):
    """Возвращает итератор генерирующий целые числа, начиная с 'x', заканчивая 'y'"""
    for i in count(x):
        yield i
        if i == y:
            break


wn_iter = whole_numbers(3, 10)  # Проверка итератора whole_numbers
print(next(wn_iter))
print(next(wn_iter))

list_numbers = [number for number in whole_numbers(3, 9)]
print(list_numbers)


#  Part2__Итератор повторяющий элементы некоторого списка определенного заранее


def func_of_cycle(elements, x):
    """Возвращаяет итератор, который повторяет по кругу элементы списка.
    elements - список
    x - количество итераций всего
    """

    k = 0
    result = []
    for i in cycle(elements):
        result.append(i)
        k += 1
        if k == x:
            break
    return iter(result)


user_list = ['Алексей', 'Сергей', 'Марина', 'Виктор']
foc_iter = func_of_cycle(user_list, 3)  # Проверка итератора func_of_cycle
print(next(foc_iter))
print(next(foc_iter))
print(next(foc_iter))

foc_list = [name for name in func_of_cycle(user_list, 16)]
print(foc_list)