from itertools import *


def f(x, y, z, w):
    return (x and ((w <= y) == z))


for x1, x2, x3, x4, x5 in product([0, 1], repeat=5):
    t = (
        # x  y   z  w
        (x1, x2, 0, 0, 1),
        (0, x3, x4, 0, 1),
        (x5, 1, 1, 1, 0)
    )

    if len(t) == len(set(t)):
        for p in permutations('xyzw', r=4):
            if all(f(**dict(zip(p, m))) == m[-1] for m in t):
                print(*p)