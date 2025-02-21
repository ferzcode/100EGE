from functools import lru_cache
@lru_cache(None)
def F(n):
    if n < 3:
        return 1
    if n > 2 and n % 2 != 0:
        return F(n - 1) - F(n - 2)
    if n > 2 and n % 2 == 0:
        summa = 0
        for i in range(1, n):
            summa += F(i)

        return summa

for n in range(0, 39):
    F(n)

print(F(39))