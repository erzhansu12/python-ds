# TODO здесь писать код
import random
class Home:
    money = 0
    food = 50
class Human:
    def __init__(self,name,hungry= 50):
        self.hungry = hungry
        self.name = name
    def eat(self):
        if Home.food >= 5:
            Home.food -=5
            self.hungry +=5
    def work(self):
        if self.hungry >= 5:
            self.hungry -=5
            Home.money +=5
    def play(self):
        if self.hungry >= 5:
            self.hungry -= 5
        else:
            self.hungry = 0
    def shopping(self):
        if Home.money >= 5:
            Home.money -=5
            Home.food +=5
    def print_info(self):
        print("У {} сыт на {}".format(self.name,self.hungry))
        print("Дома {} денег и {} еды".format(Home.money,Home.money))
person_1 = Human("Yerzhan")
person_2 = Human("Aia")
while True:
    toss = random.randint(1,6)
    if person_1.hungry < 20:
        person_1.eat()
    if person_2.hungry < 20:
        person_2.eat()
    elif Home.food < 10:
        person_2.shopping()
        person_1.shopping()
    elif Home.money < 50:
        person_2.work()
        person_1.work()
    elif toss == 1:
        person_1.work()
        person_2.work()
    elif toss == 2:
        person_1.eat()
        person_2.eat()
    else:
        person_1.play()
        person_2.play()
    if person_2.hungry <= 0 or person_1.hungry<=0:
        print("Кто то умер!")
        break
    person_1.print_info()
    person_2.print_info()

