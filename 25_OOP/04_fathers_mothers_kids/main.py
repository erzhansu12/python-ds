# TODO здесь
#  писать код
class Child:
    def __init__(self,name,age,peace = True,eat = False):
        self.name = name
        self.age = age
        self.peace = peace
        self.eat = eat
    def want_eat(self):
        self.eat = True
        print("Ребенок хочет кушать")
    def peace_stop(self):
        self.peace = False
        print("Ребенок плачет")
class Parent:
    def __init__(self,name, age,childs = []):
        self.name = name
        self.age = age
        self.childs = []
    def print_info(self):
        print("Name: {} , age: {} , children: {}".format(self.name,self.age,[child.name for child in self.childs]))
    def add_child(self,name,age):
        if age <= (self.age -16 ):
            self.childs.append(Child(name,age))
        else:
            print("Ребенок должен быть младше родителя на 16 лет")
    def eat_child(self):
        for child in self.childs:
            child.eat = False
        print("Все дети накормлены")
    def peace_child(self):
        for child in self.childs:
            child.peace = True
        print("Уффф, все дети спят")
parent1 = Parent("Yerzhan",22)
parent1.add_child("Aia",2)
parent1.print_info()
parent1.peace_child()