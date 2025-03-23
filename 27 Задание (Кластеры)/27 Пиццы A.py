def Center(cl):
    mn = []
    for x1, y1 in cl:
        s = 0
        for x2, y2 in cl:
            s += ((x1 - x2) ** 2 + (y1 - y2) ** 2) ** 0.5
        mn.append([s, x1, y1])

    s, x, y = min(mn)
    return x, y

f = open('27_Пицца_А.txt')

kl1 = []
kl2 = []

for s in f:
    x, y = [float(p) for p in s.split()]
    # y = 2 * x - 0.4
    if y < 2 * x - 0.4:
        kl1.append([x, y])
    if y > 2 * x - 0.4:
        kl2.append([x, y])

centr1 = Center(kl1)
centr2 = Center(kl2)

Px = (centr1[0] + centr2[0]) / 2
Py = (centr1[1] + centr2[1]) / 2

print(int(Px * 10000), int(Py * 10000))