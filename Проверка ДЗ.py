n = 5 * 729 ** 2024 + 3 * 243 ** 1413 - 7 * 81 ** 169 - 2 * 9 ** 107 + 3017
c = 0
while n > 0:
    cifra = n % 27
    if cifra % 2 == 0 and cifra <= 25:
        c += cifra
    n //= 27
print(c)
