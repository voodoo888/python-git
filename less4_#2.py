# Список для значений, значения который больше предыдущего значения
import random

main_list = [random.randint(1, 100) for i in range(11)]
print(main_list)
result_list = [main_list[i] for i in range(1, len(main_list)) if main_list[i] > main_list[i-1]]
print(result_list)