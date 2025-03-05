from functools import lru_cache

@lru_cache(None)
def F(n):
    if n == 1:
        return 5
    if n > 1:
        return 2 * n + 1 + F(n - 1)

for n in range(0, 2025):
    F(n)

print(F(2024) - F(2022))