with open('text3.txt', 'r', encoding='utf-8') as f_obj:
    list_staff = f_obj.readlines()


staff = [line.strip().split(' ') for line in list_staff]
sum_value = 0
filter20_value = []
for unit in staff:
    sum_value = sum_value + float(unit[1])
    if float(unit[1]) < 20000:
        filter20_value.append(unit[0])
print('Количество сотрудников: %s' % len(staff))
print('Среднее арифметическое доходов: {}'.format(sum_value / len(staff)))
print(f'Меньше 20000 получили: {", ".join(filter20_value)}.')
