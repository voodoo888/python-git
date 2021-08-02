def passport(name, surname, year_of_birth, city, email, phone):
    """Принимает данные о пользователе и выводит одной их строкой

    Именованные параметры:
    name -- Имя
    surname -- Фамилия
    year_of_birth -- год рождения
    city -- город
    email -- почта
    phone -- телефон

    """
    return f'Имя - {name}, Фамилия - {surname}, год рождения - {year_of_birth}, город - {city}, email - {email}, телефон - {phone}'


print(passport(name='Владимир', surname='Королев', year_of_birth=1988, city='Электросталь', email='developmest@gmail.com',phone='89295909300'))
