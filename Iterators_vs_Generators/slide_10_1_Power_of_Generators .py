import math


class Factorials:
    def __init__(self, stop):
        self.stop = stop
        self.n = 0

    def __iter__(self):
        return self

    def __next__(self):
        if self.n >= self.stop:
            raise StopIteration
        res = math.factorial(self.n)
        self.n += 1
        return res


for fact in Factorials(8):
    print(fact)
