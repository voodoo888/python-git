def sum_max_two(arg1, arg2, arg3):
    """ Принимает 3 аргумента и возвращает сумму наибольших двух"""
    args = [arg1, arg2, arg3]
    return sum(args) - min(args)


print(sum_max_two(40, 20, 30))
