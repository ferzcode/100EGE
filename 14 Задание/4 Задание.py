number = 15625 ** 16 - 3125 ** 3 * 25 ** 19 + 625 ** 4 - 2005
# ОБЩИЙ АЛГОС

k = 0
while number > 0:
    if number % 25 == 0:
        k += 1
    number //= 25
print(k)