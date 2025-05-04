from math import *

def Centoid(cl):
    m = [] # Точку (x, y) и расстояние до всех остальных точек

    for p1 in cl:
        c = sum(dist(p1, p2) for p2 in cl)
        m.append([c, p1])

    return min(m)[1]

cl1 = []
cl2 = []
f = open('27_A_21911.txt')
for stroka in f:
    x, y = [float(p) for p in stroka.replace(',', '.').split()]

    if y > 0:
        cl1.append([x, y])
    if y < 0:
        cl2.append([x, y])

#  0  1
# (x, y)
px1 = Centoid(cl1)[0]
px2 = Centoid(cl2)[0]
py1 = Centoid(cl1)[1]
py2 = Centoid(cl2)[1]

Px = (px1 + px2) / 2
Py = (py1 + py2) / 2
print(int(Px * 10000), int(Py * 10000))