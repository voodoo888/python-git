def clean_line(text):
    """
    Принимает текс , возвращает количество слов str --> int
    :param text: I love big apple!
    :return: 4
    """

    word_list = text.split()
    result_list = []
    for word in word_list:
        clean_word = [letter for letter in word if letter.isalpha()]
        clean_word = ''.join(clean_word)
        if clean_word:
            result_list.append(clean_word)
    return len(result_list)


with open('text2.txt', 'r', encoding='utf-8') as f_text:
    list_lines = f_text.readlines()
    count_lines = {}


num = 1
for line in list_lines:
    count_lines[num] = clean_line(line)
    num += 1
print('Всего линий : ', len(list_lines))
for keys in count_lines:
    print('Линия {} содержит {} слов'.format(keys, count_lines[keys]))
