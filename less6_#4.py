class Car:
    def __init__(self, speed, color, name, is_police=False):
        self.speed = speed
        self.color = color
        self.name = name
        if is_police:
            self.is_police = True

    def show_speed(self):
        return print(f'Скорость машины {self.name} = {self.speed} км/ч')

    def go(self):
        print(f'Машина {self.name} поехала')

    def stop(self):
        print(f'Машина {self.name} остановилась')

    def turn(self, direction):
        self.direction = direction
        print(f'Машина двигается в направлении: {self.direction}')


class TownCar(Car):
    def __init__(self, speed, color, name, is_police=False):
        super().__init__(speed, color, name, is_police)

    def show_speed(self):
        if self.speed > 60:
            print(f'Скорость машины {self.name} превышена!')
        else:
            print(f'Скорость машины {self.name} = {self.speed} км/ч')


class WorkCar(Car):
    def __init__(self, speed, color, name, is_police=False):
        super().__init__(speed, color, name, is_police)

    def show_speed(self):
        if self.speed > 60:
            print(f'Скорость машины {self.name} превышена!')
        else:
            print(f'Скорость машины {self.name} = {self.speed} км/ч')


class PoliceCar(Car):
    def __init__(self, speed, color, name, is_police=True):
        super().__init__(speed, color, name, is_police)


car1 = TownCar(150, 'red', 'bmw', False)
car1.turn('Прямо')
car1.go()
car1.stop()
print(car1.name)
car1.show_speed()
car2 = WorkCar(30, 'green', 'skoda')
car3 = PoliceCar(200, 'black', 'mercedes', True)
car3.show_speed()
print(car3.name)
car3.stop()
