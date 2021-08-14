#  Увеличение каждой первой буквы каждого слова

def int_func(word):
    """Возвращает введенное слово из маленьких букв с заглавной первой буквой"""
    result = list(word)
    result[0] = result[0].upper()
    return ''.join(result)


in_string = 'cлова написанные через один пробел в нижнем регистре'
words = in_string.split(' ')
result = [int_func(word) for word in words]
result = ' '.join(result)
print(result)
