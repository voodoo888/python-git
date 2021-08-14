# сложение введенных чисел через пробел


def upload(numbers):
    """ Принимает строку чисел через пробел --> возвращает сумму этих чисел и ключ

     Если вместо числа ввести 's' --> записывает результат, s присваивает True
     1 2 3 s --> (6, s = True)
     """

    s = False
    numbers_list = numbers.split(' ')
    result_list = []
    for i in numbers_list:
        if i == ' ' or i == '':
            continue
        elif i == 's':
            s = True
            break
        else:
            result_list.append(int(i))
    return sum(result_list), s


s = False
total_sum = 0

while s is not True:
    user_numbers = input('Введите числа через пробел: ')
    result = upload(user_numbers)
    total_sum = total_sum + result[0]
    s = result[1]
    print(total_sum)
