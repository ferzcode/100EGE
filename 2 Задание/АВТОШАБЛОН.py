from itertools import *


def f(x, y, z, w):
    return ((x == (w or z)) and (z <= (not (w or y))))


for x1, x2, x3, x4, x5, x6, x7, x8, x9, x10, x11, x12, x13 in product([0, 1], repeat=13):
    t = (
        # x  y   z  w
        (x1, 1, 1, 1, 1),
        (x2, x3, x4, x5, 1),
        (x6, x7, x8, x9, 1),
        (1, 1, x10, x11, 1),
        (x12, 0, x13, 1, 1)
    )

    if len(t) == len(set(t)):
        for p in permutations('xyzw', r=4):
            if all(f(**dict(zip(p, m))) == m[-1] for m in t):
                print(*p)