# TODO здесь писать код
class Water:
    def __add__(self, other):
        self.other = other
        if isinstance(self.other,Fire):
            return Steam
        elif isinstance(self.other,Earth):
            return Dirt
        elif isinstance(self.other, Wind):
            return Storm
        else:
            return None
class Wind:
    answer = "Шторм"
    def __add__(self, other):
        self.other = other
        if isinstance(self.other,Fire):
            return Lightning
        elif isinstance(self.other,Earth):
            return Dust
        else:
            return  None
class Fire:
    def __add__(self, other):
        self.other = other
        if isinstance(self.other,Earth):
            return Lava
        else:
            return None
class Earth:
    answer = "Earth"
class Lightning:
    answer = "Молния"
class Steam:
    answer = 'Пар'
class Storm:
    answer = "Шторм"
class Dirt:
    answer = 'грязь'
class Dust:
    answer = 'Пыль'
class Lava:
    answer = 'Лава'
a = Water()
b = Wind()
c = b + a
try:
    print(c.answer)
except AttributeError:
    print(None)