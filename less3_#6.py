#  Первая буква заглавная

def int_func(word):
    """Возвращает введенное слово из маленьких букв с заглавной первой буквой"""
    result = list(word)
    result[0] = result[0].upper()
    return ''.join(result)


food = int_func('cup-cake')
print(food)