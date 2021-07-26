# перевод время в сек
time_in_seconds = int(input('Введите время в секундах: '))
hh = time_in_seconds//3600
if hh < 10:  # внешний вид формата 00
    hh = str(f'0{hh}')
mm = (time_in_seconds % 3600)//60
if mm < 10:  # внешний вид формата 00
    mm = str(f'0{mm}')
ss = (time_in_seconds % 3600) % 60
if ss < 10:  # внешний вид формата 00
    ss = str(f'0{ss}')
print(f'{time_in_seconds} секунд это: {hh}.{mm}.{ss}')