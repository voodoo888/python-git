from abc import ABC, abstractmethod


class Clothes(ABC):
    @abstractmethod
    def material_consuption(self):
        pass


class Coat(Clothes):
    def __init__(self, V):
        self.V = V

    @property
    def material_consuption(self):
        result = self.V / 6.5 + 0.5
        return result


class Costume(Clothes):
    def __init__(self, H):
        self.H = H

    @property
    def material_consuption(self):
        result = self.H * 2 + 0.3
        return result


c = Coat(30)
d = Costume(10)
f = round((c.material_consuption + d.material_consuption), 2)
print(f)