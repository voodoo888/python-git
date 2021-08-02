# Товары структура и аналитика
command = None
structure = []
product = None  # Словарь описание о товаре
product_result = []  # Временная ячейка заполнения товара

number = 1
while True:
    command = input('Введите команду:\n '
                    '"1" - создать новый товар;\n '
                    '"2" - принять и отобразить структуру товаров.\n '
                    '"3" - отобразить аналитику\n '
                    '"0" - выход >>>')
    if command == '1':  # Заполнение товара
        name = input('Наименование товара: ')
        price = int(input('цена товара: '))
        amount = input('Количество товара: ')
        units = input('Единицы измерения: ')

        # Код добавления товара в кортеж

        product_result.clear()  # Очистка ячейки товара
        product_result.append(number)
        product = dict(Наименование=name, цена=price, Количество=amount, ед=units)
        product_result.append(product)
        structure.append(tuple(product_result))  # Добавление кортежа товара в структуру
        number += 1
        print(f'Товар "{name}" успешно добавлен под номером {number}')
    elif command == '2':  # Просмотр структуры товаров
        print(structure)
    elif command == '3':  # Аналитика и распаковка
        list_dicts = []  # это будет список товаров-словарей
        analitic_dict = {}  # Словарь для аналитики

        for goods in structure:  # Распаковка кортежей в список словарей
            dict_of_goods = goods[1]
            list_dicts.append(dict_of_goods)
        for dict_of_goods in list_dicts:  # Создание нового словаря для аналитики
            for key, value in dict.items(dict_of_goods):
                if key in analitic_dict:
                    analitic_dict[key].append(value)
                else:
                    analitic_dict[key] = [value]
        analitic_dict['ед'] = list(set(analitic_dict['ед']))  # убираем одинаковые значения Единиц изм.(как в задании)
        print(analitic_dict)
    elif command == '0':
        print('Thanks! See you later!')
        break