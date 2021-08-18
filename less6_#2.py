class Road:
    const = 25  # масса 1 кв. метра асфальта толщиной в 1 см

    def __init__(self, length, width, depth):
        self._length = length
        self._width = width
        self._depth = depth

    def mass(self):
        result = self._width * self._length * self._depth * Road.const
        return f'{self._width} метров * {self._length} метров * {Road.const} кг * {self._depth} см = {result} тонн'


a = Road(10, 20, 2)
print(a.mass())
