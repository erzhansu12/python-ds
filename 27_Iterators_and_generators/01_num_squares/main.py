# TODO здесь писать код
class Square:
    def __init__(self,N):
        self.counter =0
        self.cur_value = 1
        self.return_value = 1
        self.N = N
    def __iter__(self):
        self.counter =0
        self.cur_value = 1
        self.return_value = 1
        return self
    def __next__(self):
        self.counter +=1
        if self.counter>1:
            if self.counter >(self.N +1) :
                raise StopIteration
            self.return_value = self.cur_value ** 2
            self.cur_value +=1
        return self.return_value
def square_n(n):
    cur_value = 1
    return_value = 1
    for _ in range(n+1):
        yield return_value
        return_value = cur_value ** 2
        cur_value +=1
N = int(input())
#N_cub = Square(N)
#N_cub = square_n(N)
N_cub = (num ** 2 for num in range(1,N+1))
for i_sq in N_cub:
    print(i_sq)
