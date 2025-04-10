from math import dist

def Centroid(kl):
    m = []
    for p1 in kl:
        sm = sum(dist(p1, p2) for p2 in kl)
        m.append([sm, p1])
    return min(m)[1]

kl1 = []
kl2 = []
kl3 = []

for p in open('27_B_21425.txt'):
    x, y = [float(x) for x in p.split()]

    if y > 0 and x > 0:
        kl1.append([x, y])
    if y < 0 and x > 0:
        kl2.append([x, y])
    if x < 0:
        kl3.append([x, y])

Px = (Centroid(kl1)[0] + Centroid(kl2)[0] + Centroid(kl3)[0]) / 3
Py = (Centroid(kl1)[1] + Centroid(kl2)[1] + Centroid(kl3)[1]) / 3

print(int(Px * 10000), int(Py * 10000))

