# записывать построчно информацию вводимую пользователем
f_obj = open('text1.txt', 'w', encoding='utf-8')
data = True
while data:
    data = input('Введите данные: ')
    print(data, file=f_obj)
