def Center(cl):
    mn = []
    for x1, y1 in cl:
        s = 0
        for x2, y2 in cl:
            s += ((x1 - x2) ** 2 + (y1 - y2) ** 2) ** 0.5
        mn.append([s, x1, y1])

    s, x, y = min(mn)
    return x, y


f = open('27_Пицца_В.txt')

kl1 = []
kl2 = []
kl3 = []
kl4 = []

k = 0
for s in f:
    k += 1
    x, y = [float(p) for p in s.split()]

    if y < -2 * x + 24:
        kl1.append([x, y])
    if y > -2 * x + 24 and y > 3 * x - 26:
        kl2.append([x, y])
    if y > -2 * x + 24 and y < 3 * x - 26 and y > 0.625 * x - 2.25:
        kl3.append([x, y])
    if y > -2 * x + 24 and y < 3 * x - 26 and y < 0.625 * x - 2.25:
        kl4.append([x, y])

centr1 = Center(kl1)
centr2 = Center(kl2)
centr3 = Center(kl3)
centr4 = Center(kl4)

Px = (centr1[0] + centr2[0] + centr3[0] + centr4[0]) / 4
Py = (centr1[1] + centr2[1] + centr3[1] + centr4[1]) / 4

print(int(Px * 10000), int(Py * 10000))