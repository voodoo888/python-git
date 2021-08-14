def cleaner(word):
    """
    Получает строку оставляет только цифры. str --> int
    :param word: 13(пр)
    :return: 13
    """
    new_word = []
    for letter in word:
        if letter.isdigit():
            new_word.append(letter)
    result = ''.join(new_word)
    if len(result) > 0:
        result = int(result)
    else:
        result = 0
    return result


result_dict = {}

with open('text6.txt', 'r', encoding='utf-8') as f_data:
    for line in f_data.readlines():
        line_point = line.find(': ')
        subject = line[:line_point]
        result_lessons = sum([cleaner(num) for num in line[line_point:].split(' ')])
        result_dict[subject] = result_lessons

print(result_dict)
