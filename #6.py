# Количество километров - найти номер дня?

number_a = float(input('Введите стартовое количество километров в день: '))
number_b = float(input('Введите желаемое количество километров в день: '))
days = 1
while number_a < number_b:
    number_a = number_a * 1.1
    days += 1
print('Вы достигнете желаемого результата на {}-й день'.format(days))