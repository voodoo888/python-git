class Stationery:
    def __init__(self, title=None):
        if title == None:
            self.title = input('Название: ')
        else:
            self.title = title

    def draw(self):
        print('Запуск отрисовки.')


class Pen(Stationery):
    def draw(self):
        print(f'(Pen draw)Началась отрисовка предметом {self.title}')


class Pencil(Stationery):
    def draw(self):
        print(f'(Pencil draw) Началась отрисовка предметом {self.title}')


class Hendle(Stationery):
    def draw(self):
        print(f'(Hendle draw) Началась отрисовка предметом {self.title}')


s = Stationery()
s.draw()
pen = Pen('Ручка')
pen.draw()
pencil = Pencil('Карандаш')
pencil.draw()
hendle = Hendle()
hendle.draw()
