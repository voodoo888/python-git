# Время года в ответ на месяц
user_month = int(input('Введите порядковый номер месяца от 1 до 12: '))
seasons = dict(Зима=[12, 1, 2],
               Весна=[3, 4, 5],
               Лето=[6, 7, 8],
               Осень=[9, 10, 11])
for key in seasons.keys():
    if user_month in seasons.get(key):
        result = key
print(result)
