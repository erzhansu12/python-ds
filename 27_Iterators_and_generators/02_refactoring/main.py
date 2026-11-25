list_1 = [2, 5, 7, 10]
list_2 = [3, 8, 4, 9]
to_find = 56
def find_1(to_find):
    for x in list_1:
        for y in list_2:
            result = x * y
            print(x, y, result)
            if result  == to_find:
                raise  StopIteration("FOUND!!!")
            yield  result

gen = find_1(to_find)
for i in gen:
    print(i)
# TODO провести рефакторинг кода
