from math import dist
#
# clustersA = [[], []]
# clustersB = [[], [], []]
#
# for s in open('27_A_20911.txt'):
#     x, y = [float(k) for k in s.split()]
#     if y > 0:
#         clustersA[0].append([x, y])
#     if y < 0:
#         clustersA[1].append([x, y])
#
# for s in open('27_B_20911.txt'):
#     x, y = [float(k) for k in s.split()]
#     if y < -6:
#         clustersB[0].append([x, y])
#     if y > -6 and y < 5.9:
#         clustersB[1].append([x, y])
#     if y > 5.9:
#         clustersB[2].append([x, y])
#
# def center(cl):
#     m = []
#     for p in cl:
#         summ_dist = 0
#         count = 0
#         for p1 in cl:
#             if dist(p, p1) <= 1:
#                 summ_dist += dist(p, p1)
#                 count += 1
#         m.append([summ_dist/count, p])
#     return min(m)[1]
#
#
# centersA = [center(kl) for kl in clustersA]
# centersB = [center(kl) for kl in clustersB]
#
# PxA = sum(x for x, y in centersA) / 2
# PyA = sum(y for x, y in centersA) / 2
# PxB = sum(x for x, y in centersB) / 3
# PyB = sum(y for x, y in centersB) / 3
# print(int(abs(PxA * 10000)), int(abs(PyA * 10000)))
# print(int(abs(PxB * 10000)), int(abs(PyB * 10000)))


def isolate(cl):
    m = []
    for p in cl:
        count = 0
        for p1 in cl:
            if dist(p, p1) <= 1:
                count += 1
        m.append([count, p])
    return min(m)[1]

def diametr(cl):
    m = []
    for p in cl:
        for p1 in cl:
            if p != p1:
                m.append([dist(p, p1), p])
    return max(m)[0]

def centoid(cl):
    summ_x = 0
    summ_y = 0

    for p in cl:
        summ_x += p[0]
        summ_y += p[1]

    return [summ_x / len(cl), summ_y / len(cl)]

def mediana(cords):
    m = []
    for c in cords:
        menshe = 0
        bolshe = 0
        for c1 in cords:
            if c1 != c1:
                if c1 < c:
                    menshe += 1
                else:
                    bolshe += 1
        if menshe == bolshe:
            m.append(c)
    return m

mediana(p for p in cl[0])
mediana(p for p in cl[1])





























