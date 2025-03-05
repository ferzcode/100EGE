# print("x y z w")
# for x in range(2):
#     for y in range(2):
#         for z in range(2):
#             for w in range(2):
#                 F = (not(x <= y)) or (x == z) or w
#                 if F == 0:
#                     print(x, y, z, w)

from itertools import *


def u(x, y, w, z):
    return (not (x <= y)) or (x == z) or w


for x1, x2, x3, x4, x5, x6 in product([0, 1], repeat=6):
    t = ((1, 0, x1, 1, 0),
         (x2, x3, 1, 1, 0),
         (x4, x5, 1, x6, 0))
    if len(t) == len(set(t)):
        for p in permutations("xywz", r=4):
            if all(u(**dict(zip(p, m))) == m[-1] for m in t):
                print(*p)