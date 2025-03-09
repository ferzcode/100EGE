number = 1331 ** 650 - 55 * 121 ** 610 + 77 * 11 ** 510 - 3 * 11 ** 100 - 221

k = 0
while number > 0:
    if number % 11 == 10:
        k += 1
    number //= 11
print(k)