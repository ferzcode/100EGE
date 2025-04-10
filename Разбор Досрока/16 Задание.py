from functools import *
from sys import *

setrecursionlimit(10000)
@lru_cache(None)
def F(n):
    if n <= 5: return 1
    if n > 5: return n + F(n - 2)

for n in range(0, 2127):
    F(n)

print(F(2126) - F(2122))