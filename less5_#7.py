import json


def format_line(line):
    """
    Принимает строку формата (firm_1 ООО 10000 5000)
    Выдает кортеж: (name-наменование, profit-прибыль)

    :param line:firm_1 ООО 10000 5000
    :return:name = firm_1, profit = (10000-5000)
    """

    list_of_line = line.split(' ')
    name = list_of_line[0]
    profit = int(list_of_line[2]) - int(list_of_line[3])
    return name, profit


firms_dict = {}
profit_firms = {}
losses_firms = {}

with open('text7.txt', 'r', encoding='utf-8') as f_obj:
    for line in f_obj:
        data_of_line = format_line(line)
        firms_dict[data_of_line[0]] = data_of_line[1]
        if data_of_line[1] >= 0:
            profit_firms[data_of_line[0]] = data_of_line[1]
        else:
            losses_firms[data_of_line[0]] = data_of_line[1]


average_value = sum(profit_firms.values()) / len(profit_firms)
average_profit = dict(average_profit=round(average_value, 2))
result_list = [profit_firms, average_profit, losses_firms]


with open('data7.json', 'w', encoding='utf-8') as write_f:  # Сохранение в json
    json.dump(result_list, write_f)

print('Все фирмы: ', firms_dict)
print('Итоговый список: ', result_list)  # Печать списка в качестве примера для просмотра
print('Итоговый список json: ', json.dumps(result_list))  # Печать списка.json в качестве примера для просмотра
