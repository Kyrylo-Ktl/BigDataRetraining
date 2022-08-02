import math


def Factorials(stop):
    for i in range(stop):
        yield math.factorial(i)


for fact in Factorials(8):
    print(fact)
