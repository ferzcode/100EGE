# Задача №17953

def Gravity(p1, p2):
    dist = ((p2[0] - p1[0]) ** 2 + (p2[1] - p1[1]) ** 2) ** 0.5
    mr = abs(p2[2] - p1[2])

    return dist * mr

def Centroid(kl):
    m = []
    for p1 in kl: # x y g
        sm = sum(Gravity(p1, p2) for p2 in kl)
        m.append([sm, p1])

    return min(m)[1]


for p in open('27_B_21425.txt'):
    x, y, g = [float(x) for x in p.split()]

