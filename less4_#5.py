from functools import reduce


def muli_culc(prev_num, num):
    """Перемножает предыдущее число в списке со следующим
    prev_num - предыдущее число
    num - следующее число
    """

    return prev_num * num


numbers = [number for number in range(100, 1001, 2)]
print(reduce(muli_culc, numbers))
