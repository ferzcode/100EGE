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


f = open('27_A_Апробация.txt')

kl1 = []
kl2 = []

for s in f:
    x, y = [float(p) for p in s.split()]
    # print(x, y)

    if x > 0 and y > 0:
        kl1.append([x, y])
    if x < 0 and y < 0:
        kl2.append([x, y])

x1, y1 = Center(kl1)
x2, y2 = Center(kl2)

Px = (x1 + x2) / 2
Py = (y1 + y2) / 2

print(int(Px * 10000), int(Py * 10000))