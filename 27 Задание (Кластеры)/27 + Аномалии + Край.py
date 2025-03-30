from math import *


def Kray(cl):
    mn = []
    for x1, y1 in cl:
        s = 0
        for x2, y2 in cl:
            s += ((x1 - x2) ** 2 + (y1 - y2) ** 2) ** 0.5
        mn.append([s, x1, y1])

    s, x, y = max(mn)
    return x, y


f = open('27_Anomaly_B.txt')
kl1 = []
kl2 = []
kl3 = []
kl4 = []
kl5 = []

for s in f:
    x, y = [float(p) for p in s.split()]

    if -40 < x < -21 and 45 < y < 110:
        kl1.append([x, y])
    if -15 < x < 5 and 45 < y < 110:
        kl2.append([x, y])
    if 0 < x < 20 and -30 < y < 30:
        kl3.append([x, y])
    if -30 < x < -10 and -30 < y < 30:
        kl4.append([x, y])
    if -55 < x < -35 and -30 < y < 30:
        kl5.append([x, y])


kray1 = Kray(kl1)
kray2 = Kray(kl2)
kray3 = Kray(kl3)
kray4 = Kray(kl4)
kray5 = Kray(kl5)

Tx = (kray1[0] + kray2[0] + kray3[0] + kray4[0] + kray5[0]) / 5
Ty = (kray1[1] + kray2[1] + kray3[1] + kray4[1] + kray5[1]) / 5
print(int(Tx * 10000), int(Ty * 10000))
