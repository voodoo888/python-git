class Worker:
    def __init__(self, name, surname, position, wage, bonus):
        self.name = name
        self.surname = surname
        self.position = position
        dict_income = {'wage': wage, 'bonus': bonus}
        self._income = dict_income


class Position(Worker):
    def __init__(self, name, surname, position, wage, bonus):
        super().__init__(name, surname, position, wage, bonus)

    def get_full_name(self):
        return print(f'Имя - {self.name}, фамилия - {self.surname}')

    def get_full_income(self):
        result = self._income['wage'] + self._income['bonus']
        return print(result)


man1 = Position('Jon', 'Mccouni', 'ingener', 5000, 300)
man2 = Position('Mary', 'Cramberry', 'director', 8000, 200)

man1.get_full_name()
man1.get_full_income()
print(man1.position)
print(man1._income)

man2.get_full_name()
man2.get_full_income()
print(man2.position)
print(man2._income)