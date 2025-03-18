from math import ceil

otrezok = []

for x in [k * 0.25 for k in range(-10000, 10000)]:
    A = 0
    P = 8 <= x <= 39
    Q = 23 <= x <= 58

    f = ((P or A) <= (Q or A))
    if f != 1:
        otrezok.append(x)

print(ceil(max(otrezok) - min(otrezok)))