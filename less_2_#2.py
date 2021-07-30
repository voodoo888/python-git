# Перемена мест значений списка по соседним индексам
my_list_string = input('Введите значения списка через запятую: ')
my_list = my_list_string.split(',')
result_list = []  # Список для вывода результата
pair = []  # Создание списка для пары
for el in range(len(my_list)-1):
    pair = [my_list[el+1], my_list[el]]
    if el % 2 == 0:
        result_list.extend(pair)
if len(my_list) % 2 != 0:
    result_list.append(my_list[-1])
print(f'Исходные данные: {my_list}')
print(f'Результат преобразования: {result_list}')