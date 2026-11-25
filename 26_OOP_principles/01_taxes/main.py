# TODO здесь писать код
class Property:
    def __init__(self,worth):
        self.worth = worth
    def taxes(self):
        return  self.worth * 0.1
class Appartment(Property):
    def __init__(self, worth):
        super().__init__(worth)
    def taxes(self):
        return self.worth /1000
class Car(Property):
    def __init__(self, worth):
        super().__init__(worth)
    def taxes(self):
        return self.worth /200
class CountryHouse(Property):
    def __init__(self, worth):
        super().__init__(worth)
    def taxes(self):
        return self.worth /500
while True:
    try:
        money = int(input("Введите количество денег:"))
        riches = int(input("Введите стоимость своего имущества:"))
        type = int(input("1-машина, 2 - дача, 3 - дом  "))
        if type == 1:
            car = Car(riches)
            tax = car.taxes()
            print("Ваш налог: {}".format(tax))
            if tax > money:
                print("Вам не хватает: {}".format(tax - money))
        elif type == 1:
            ch = CountryHouse(riches)
            tax = ch.taxes()
            print("Ваш налог: {}".format(tax))
            if tax > money:
                print("Вам не хватает: {}".format(tax - money))
        if type == 3:
            house =Appartment(riches)
            tax = house.taxes()
            print("Ваш налог: {}".format(tax))
            if tax > money:
                print("Вам не хватает: {}".format(tax - money))
    except ValueError:
        print("Введите число")
