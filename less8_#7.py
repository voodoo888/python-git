class Complex:
    def __init__(self, a, b):
        self.a = a
        self.b = b

    def __str__(self):
        return (f'({self.a} + {self.b}i)')

    def __add__(self, other):
        a = self.a + other.a
        b = self.b + other.b
        return Complex(a, b)

    def __mul__(self, other):
        a = (self.a * other.a) - (self.b * other.b)
        b = (self.a * other.b) + (other.a * self.b)
        return Complex(a, b)


z = Complex(2, 3)
print(z)
y = Complex(2, 2)
print(z + y)
print(z * y)
