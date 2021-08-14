rus_num = {'1': 'Один', '2': 'Два', '3': 'Три', '4': 'Четыре', '5': 'Пять', '6': 'Шесть'}
with open('text4-1.txt', 'r') as f_obj:
    lines_list = f_obj.readlines()
    lines_clean = []
    for line in lines_list:
        lines_clean.append(line.strip().split('-'))

for keys in rus_num:
    for line in lines_clean:
        if keys == line[1]:
            line[0] = rus_num[keys]

with open('text4-2.txt', 'w', encoding='utf-8') as new_obj:
    for lines in lines_clean:  # Добавление перевода в новый файл
        new_line = '-'.join(lines) + '\n'
        new_obj.write(new_line)
