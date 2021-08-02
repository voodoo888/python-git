# Рейтинг
user_number = None
rating = [7, 5, 3, 3, 2]
while True:
    user_number = input('Введите число или команду "end": ')
    if user_number == 'end':
        break
    user_number = int(user_number)
    rating.append(user_number)
    rating.sort()
    rating.reverse()
    print(rating)