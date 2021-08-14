#  Удаление повторов

default_list = [2, 2, 2, 5, 14, 53, 10, 9, 10, 67, 54, 53, 14, 100, 156, 23, 4]
result_list = [el for el in default_list if default_list.count(el) == 1]
print(default_list)
print(result_list)