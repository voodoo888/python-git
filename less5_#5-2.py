# Номер 5 - вариант 2
f_obj = open('text5-2.txt', 'w')
numbers = input('введите числа разделенные пробелами: ')
f_obj.write(numbers)
f_obj.close()
f_obj = open('text5.txt', 'r')
numbers_in = f_obj.read()
result = sum([int(num) for num in numbers.strip().split(' ')])
print(result)
