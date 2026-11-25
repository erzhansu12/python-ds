# TODO здесь писать код
class Potato:
    states = {0: "Отсутствует",1:"Росток",2:"Зеленая",3:"Зрелая"}
    def __init__(self,index):
        self.index = index
        self.state = 0
    def grow(self):
        if self.state < 3:
            self.state +=1
        self.print_state()
    def  is_ripe(self):
        if self.state == 3:
            return  True
        return False
    def print_state(self):
        print("Картошка {} сейчас на {}".format(self.index,Potato.states[self.state]))
class PotatoGarden:
    def __init__(self,count):
        self.potatoes = [Potato(index) for index in range(1,count+1)]
    def grow_all(self):
        print("Картошка растет")
        for i_potato in self.potatoes:
            i_potato.grow()
    def are_all_ripe(self):
        for i_potato in self.potatoes:
            if not all([i_potato.is_ripe() for i_potato in self.potatoes]):
                return False
            else:
                return True
class Gardener:
    def __init__(self,name,garden_count):
        self.name = name
        self.garden = PotatoGarden(garden_count)
    def take_care(self):
        self.garden.grow_all()
    def harven(self):
        if self.garden.are_all_ripe():
            self.garden.potatoes = []
            print("Урожай собран")
        else:
            print("Не время для урожая. Продалжайте ухаживать")
grd = Gardener("Yerzhan",50)
for i in range(4):
    grd.take_care()
grd.harven()
print(grd.garden.potatoes)