# Пользователь вводит строку, резделить по словам через пробел, каждое слово с новой строки, срез длины 10 симв
user_string = input('Введите произвольный текст: ')
result = user_string.split(' ')
for number, word in enumerate(result, 1):
    print(number, word[:10])