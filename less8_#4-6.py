class Warehouse:
    def __init__(self):
        self.data = {}

    def accept(self, element, count=1):
        if element.name not in self.data:
            self.data[element.name] = count
        else:
            self.data[element.name] += count

    def betray(self, element, count):
        if element.name not in self.data:
            print(f'{element.name} на складе отсутствует')
        elif self.data[element.name] < count:
            print(f'На складе есть только не достаточное количество техники')
        else:
            self.data[element.name] -= count
        pass


class OfficeEquipment:
    def __init__(self, name, price, color):
        self.name = name
        try:
            if type(price) is not int:
                raise ValueError('Неверное значение цены!')
            else:
                self.price = price
        except ValueError as err:
            print(err)
        self.color = color


class Printer(OfficeEquipment):
    def __init__(self, name, price, color, laser=True):
        super().__init__(name, price, color)
        self.laser = laser


class Scanner(OfficeEquipment):
    def __init__(self, name, price, color, speed):
        super().__init__(name, price, color)
        self.speed = speed


class Copier(OfficeEquipment):
    def __init__(self, name, price, color, power):
        super().__init__(name, price, color)
        self.power = power


wildberry = Warehouse()

p = Printer('Canon', 2000, 'red', 200)
wildberry.accept(p, 3)
wildberry.accept(p, 4)
wildberry.betray(p, 6)
print(wildberry.data)
cop = Copier('Xerox', '200t', 'black', 300)
wildberry.accept(cop, 1)
print(wildberry.data)
