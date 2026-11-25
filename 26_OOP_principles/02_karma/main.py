# TODO здесь писать код
import random as rd


class KillError(BaseException):
    def __init__(self, msg):
        super().__init__(msg)
class DrunkError(BaseException):
    def __init__(self, msg):
        super().__init__(msg)
class CarCrashError(BaseException):
    def __init__(self, msg):
        super().__init__(msg)
class GluttonyError(BaseException):
    def __init__(self, msg):
        super().__init__(msg)
class DepressionError(BaseException):
    def __init__(self, msg):
        super().__init__(msg)

class Budda:
    def __init__(self):
        self.__karma = 400
    def get_carma(self):
        return self.__karma
    def one_day(self):
        excep = rd.randint(1,10)
        if excep != 10:
            self.__karma += rd.randint(1,7)
        else:
            try:
                extp = rd.randint(1,5)
                if extp == 1:
                    raise KillError("Вы убили кого то")
                elif extp == 2:
                    raise DrunkError("Я набухался")
                elif extp == 3:
                    raise CarCrashError("ДТП")
                elif extp == 4:
                    raise GluttonyError("Нажрался")
                elif extp == 5:
                    raise DepressionError("Почему все против меня!")
            except KillError:
                print(KillError,'Вы убили кого то')
            except DrunkError:
                print(DrunkError,"UHHH")
            except CarCrashError:
                print(CarCrashError,"CRASHH!!!")
            except GluttonyError:
                print(GluttonyError,"AHHHH")
            except DepressionError:
                print(DepressionError,"DEAD!")
buddist = Budda()
day = 1
while buddist.get_carma() < 500:
    print("День {}".format(day))
    buddist.one_day()
    print("Карма: ",buddist.get_carma())
    day +=1