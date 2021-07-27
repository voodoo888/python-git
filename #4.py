# найти самую большую цифру в числе

number = input('Введите некое число: ')
number_one = int(number[0])
i = 1
a = len(number)  # Количество итераций
while i < a:
    if number_one <= int(number[i]):
        number_one = int(number[i])
    i += 1
print(f'Наибольшая цифра: {number_one}')

# Вариант 2

number_max = 0
number = int(number)
while number:
    result = number % 10
    if result > number_max:
        number_max = result
    number = number // 10
print('Масимальная цифра (вариант 2): ', number_max)