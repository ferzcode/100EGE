from functools import lru_cache

@lru_cache(None)
def F(n):
    if n == 1:
         return 1
    if n > 1:
        return n + F(n - 1)

for n in range(2024):
    F(n)

count = 0

fu = F(2023)
for n in range(1, 101):
    if (fu // F(n)) % 2 == 0:
        count += 1

print(count)