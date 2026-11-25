# TODO здесь писать код
import  random
class Warrior:
    health = 100
    def attack(self):
        self.health -= 20
player_1 = Warrior()
player_2 = Warrior()
while True:
    who_attack = random.randint(1,2)
    if who_attack == 1:
        player_2.attack()
        if player_2.health <= 0:
            print("Выиграл 1 воин")
            break
        else:
            print("Атаковал 1 воин, у 2 воина осталось {} здоровья".format(player_2.health))
    else:
        player_1.attack()
        if player_1.health <= 0:
            print("Выиграл 2 воин")
            break
        else:
            print("Атаковал 2 воин, у 1 воина осталось {} здоровья".format(player_2.health))