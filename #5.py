# Вводные данные выручки и издержек
proceed = float(input('Введите значение выручки: '))
costs = float(input('Введите значение издержек: '))

# расчет результата
result = False
result_one = None
if proceed > costs:
    print('Фирма работает в прибыль.')
    result = True
elif proceed < costs:
    print('Фирма работает в убыток.')
else:
    print('Фирма работает в ноль.')
if result:
    profit = proceed-costs
    result = profit/proceed
    print('Рентабельность фирмы = %.2f ' % result)
    staff = int(input('Введите количество сотрудников: '))
    profit_one = profit/staff
    print('Прибыль на одного сотрудника составит: %.2f' % profit_one)