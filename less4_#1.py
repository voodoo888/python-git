# Скрипт расчета зп сотрудника с параметрами argv
from sys import argv
script_name, working_out, rate_per_hour, prize = argv


def calc():
    total = float(working_out)*float(rate_per_hour)+float(prize)
    return total


print(calc())