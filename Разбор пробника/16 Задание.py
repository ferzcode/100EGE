from sys import *
from functools import *
setrecursionlimit(10000)

@lru_cache(None)
def F(n):
    if n == 1:
        return 1
    if n % 2 == 0:
        return n + 3 * F(n - 1)
    if n > 1 and n % 2 != 0:
        return 2 + 2 * F(n - 2)

for n in range(1, 24):
    F(n)

print(F(23))