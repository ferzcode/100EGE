from math import *

def Center(cl):
    mn = []
    for x1, y1 in cl:
        s = 0
        for x2, y2 in cl:
            s += ((x1 - x2) ** 2 + (y1 - y2) ** 2) ** 0.5
        mn.append([s, x1, y1])

    s, x, y = min(mn)
    return x, y


f = open('27_B_ЕГКР2024.txt')

kl1 = []
kl2 = []
kl3 = []

for s in f:
    x, y = [float(p) for p in s.split()]

    if y > 8:
        kl1.append([x, y])
    if y < 7 and x > 0:
        kl2.append([x, y])
    if y < 4 and x < 0:
        kl3.append([x, y])


x1, y1 = Center(kl1)
x2, y2 = Center(kl2)
x3, y3 = Center(kl3)

Px = (x1 + x2 + x3) / 3
Py = (y1 + y2 + y3) / 3

print(abs(int(Px * 10000)), abs(int(Py * 10000)))