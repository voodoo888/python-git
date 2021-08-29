class Cell:
    def __init__(self, count_cells):
        self.count_cells = int(count_cells)

    def __add__(self, other):
        result = self.count_cells + other.count_cells
        return Cell(result)

    def __sub__(self, other):
        if self.count_cells > other.count_cells:
            result = self.count_cells - other.count_cells
            return Cell(result)
        else:
            return print("Операция невыполнима")

    def __mul__(self, other):
        result = self.count_cells * other.count_cells
        return Cell(result)

    def __truediv__(self, other):
        result = self.count_cells // other.count_cells
        return Cell(result)

    def make_order(self, cells_in_row):
        k = 0
        result = ''
        while k < self.count_cells:
            if k % cells_in_row == 0 and k != 0:
                result = result + '\n'
            k += 1
            result = result + '*'
        return repr(result)

a = Cell(10)
b = Cell(5)
c = Cell(15)
d = a + b
print(d.count_cells)
d = a - b
print(d.count_cells)
d = b - a
d = a * b
print(d.count_cells)
d = a / b
print(d.count_cells)
print(a.count_cells)
print(a.make_order(5))
