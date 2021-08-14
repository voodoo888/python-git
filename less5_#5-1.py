# Номер 5 вариант 1
with open('text5-1.txt', 'w+') as f_obj:
    try:
        numbers = input('введите числа разделенные пробелами: ')
        f_obj.write(numbers)
        f_obj.seek(0)
        numbers_in = f_obj.read()
        result = sum([int(num) for num in numbers.strip().split(' ')])
        print(result)
    except ValueError:
        print('Неправильный ввод! Вводить надо числа, разделенные одним пробелом.')