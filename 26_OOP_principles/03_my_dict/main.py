# TODO здесь писать код
class MyDict(dict):
    def gett(self,key):
        if self.get(key) is None:
            return  0
        else:
            self.get(key)
dict = {0:"Aloo"}
my_dict = MyDict(dict)
print(my_dict.gett(2))