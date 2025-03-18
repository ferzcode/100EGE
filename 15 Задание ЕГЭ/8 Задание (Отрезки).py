otrezok = []

from math import ceil

for x in [k * 0.25 for k in range(-10000, 10000)]:
    A = 1 # 0 - наименьшее / 1- наибольшее
    P = 25 <= x <= 50
    Q = 32 <= x <= 47

    f = (((not A) <= P) <= (A <= Q))

    if f != 0: # Если найти наименьшее  и ф-ция истина - 1, если найти наименьшее и ф-ция ложь - 0.
        # Если найти наибольшее и ф-ция истина - 0, если найти наибольшее и ф-ция ложь - 1
        otrezok.append(x)
print(ceil(max(otrezok) - min(otrezok)))