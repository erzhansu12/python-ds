# TODO здесь писать код
import math
class Auto:
    def __init__(self,direction = 1):
        self.direction = direction
        self.x = 0
        self.y = 0
    def move(self,change = 0):
        if change == 0:
            self.x +=1
        else:
            print("1-прямо, 2 - вниз, 3-налево, 4 - направо")
            self.direction = input("Введите направление:")
            if self.direction == 1 or self.direction == 2:
                self.x += 1
            else:
                self.y += 1
    def total_road(self):
        return  math.sqrt(self.x ** 2 + self.y ** 2)
class Bus(Auto):
    def __init__(self,passengers = 0 , money = 0):
        super().__init__()
        self.passengers = passengers
        self.money = money
    def pass_in(self,passengers):
        self.passengers += passengers
    def pass_out(self,passengers):
        self.passengers -= passengers

    def move(self, change=0):
        if change == 0:
            self.x += 1
        else:
            print("1-прямо, 2 - вниз, 3-налево, 4 - направо")
            self.direction = input("Введите направление:")
            if self.direction == 1 or self.direction == 2:
                self.x += 1
            else:
                self.y += 1
        self.money = self.passengers * 150 + self.total_road() * 50
school = Bus()
school.pass_in(30)
school.move(1)
print(school.money)