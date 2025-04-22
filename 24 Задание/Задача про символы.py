from sys import *
from functools import *

setrecursionlimit(10000)

@lru_cache(None)
def f(n):
    if n < 3:
        return n
    if n > 2 and n % 2 != 0:
        return f(n - 1) + f(n - 2) + 1
    if n > 2 and n % 2 == 0:
        # return sum(f(n) for n in range(1, n))
        summa = 0
        for i in range(1, n):
            summa += f(i)
        return summa


for n in range(38):
    f(n)

print(f(38))
