# TODO здесь писать код
import  math
class Circle:
    def __init__(self,r=1,x=0,y=0):
        self.r = r
        self.x = x
        self.y = y
    def area(self):
        return math.pi * (self.r ** 2)
    def perimetr(self):
        return math.pi * 2 * self.r
    def raiseup(self,k=1):
        self.r = self.r * k
    def intersect(self,x,y,r):
        if self.x == x:
            if self.r + r > abs(self.y - y):
                print('Окружности пересекаются')
            else:
                print('Окружности не пересекаются')
        elif self.y == y:
            if self.r + r > abs(self.x - x):
                print('Окружности пересекаются')
            else:
                print('Окружности не пересекаются')
        else:
            if (self.r + r) ** 2 > abs((self.x - x) ** 2 - (self.y - y) ** 2):
                print('Окружности пересекаются')
            else:
                print('Окружности не пересекаются')
circle1 = Circle(r=3,x=2,y=1)
circle2 = Circle(r=1,x=2,y=1)
circle2.raiseup(2)
print(circle1.area())
print(circle2.perimetr())
circle1.intersect(circle2.x,circle2.y,circle2.r)