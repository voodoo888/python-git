list_of_lists = [[1, 2, 3], [10, 20, 30], [100, 200, 300]]


class Matrix:
    def __init__(self, matrix):
        self.matrix = matrix

    def __str__(self):
        result = ''
        limit = len(self.matrix)
        i = 0
        while i < limit:
            row = []
            for el in self.matrix[i]:
                row.append(str(el).rjust(10))
            result = result + ''.join(row) + '\n'
            i += 1
        return result

    def __add__(self, other):
        for i in range(len(self.matrix)):
            for j in range(len(self.matrix[0])):
                self.matrix[i][j] = self.matrix[i][j] + other.matrix[i][j]
        return Matrix(self.matrix)


a = Matrix(list_of_lists)
b = Matrix(list_of_lists)
print(a)
print(b)
c = a + b
print(c)
