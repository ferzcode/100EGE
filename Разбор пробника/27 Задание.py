from math import dist

def Centroid(kl):
    m = []
    for p in kl:
        summa = 0
        for p1 in kl:
            summa += dist(p, p1)
        m.append([summa, p])
    return min(m)[1]

kl1 = []
kl2 = []
kl3 = []
for s in open('27B.txt'):
    x, y = [float(p) for p in s.replace(',', '.').split()]

    if x > 0 and y > 0:
        kl1.append([x, y])
    if x < 0 and y < 0:
        kl2.append([x, y])
    if x < 0 and y > 0:
        kl3.append([x, y])

center1 = Centroid(kl1)
center2 = Centroid(kl2)
center3 = Centroid(kl3)
Px = (center1[0] + center2[0] + center3[0]) / 3
Py = (center1[1] + center2[1] + center3[1]) / 3

print(int(abs(Px * 10000)), int(abs(Py * 10000)))