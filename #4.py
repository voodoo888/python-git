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