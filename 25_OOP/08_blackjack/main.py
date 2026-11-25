# TODO здесь писать код
import random
class BlackJack:
     # Индексы с 1 - 9 цифры, 0 - Туз,10 - Валет, 11 - Дама,12-Король
    cards = [
        [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13], #буби
        [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13], #крести
        [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13], #черви
        [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13]  #пики
    ]
    def __init__(self,sum =0):
        self.sum =sum
    def start_play(self):
        for i in range(2):
            mast = random.randint(0,3)
            card = random.randint(0,len(self.cards[mast]))
            if self.cards[mast][card] != 0:
                self.sum += self.cards[mast][card]
                self.cards[mast][card] = 0
                print(self.sum)
    def action(self):
        while True:
            if self.sum > 21:
                print("Вы проиграли")
                break
            print("Взять карту или хватит?(1-взять, 2 - хватит)",end="  ")
            action = int(input())
            if action == 1:
                mast = random.randint(0, 3)
                card = random.randint(0, 12)
                if self.cards[mast][card] != 0:
                    self.sum += self.cards[mast][card]
                    self.cards[mast][card] = 0
                    print(self.sum)
                elif self.cards[mast][card] == 0:
                    print("Выберите другую карты")
            else:
                    self.finish()
                    break
    def finish(self):
        diller = 0
        while diller < 21:
            mast = random.randint(0, 3)
            card = random.randint(0, len(self.cards[mast]))
            if self.cards[mast][card] != 0:
                diller += self.cards[mast][card]
                del self.cards[mast][card]
        if diller > 21 or diller < self.sum:
            print("Вы выиграли!")
        elif diller > self.sum:
            print("Вы проиграли")
CaesarPalace = BlackJack()
print(CaesarPalace.cards)
CaesarPalace.start_play()
CaesarPalace.action()