# int() - ВСЕГДА в меньшую сторону 9.9999999
# round() - округление по правилам математики 3.51 = 4, 4.49 = 4 01234 - В МЕНЬШУЮ, 56789 - В БОЛЬШУЮ

# from math import *
# ceil() - ВСЕГДА в бОльшую сторону


from math import *

def f(s1, s2, m):
    if s1 + s2 <= 72: return m % 2 == 0
    if m == 0: return 0

    h = [f(s1 - 3, s2, m - 1), f(s1, s2 - 3, m - 1), f(ceil(s1 / 2), s2, m - 1), f(s1, ceil(s2 / 2), m - 1)]
    return any(h) if m % 2 != 0 else any(h)

# 19 - 188
# 20 - 51, 100
# 21 - 103

# 1234
# ПВПВ

print('19: ', [s2 for s2 in range(23, 1000) if f(50, s2, 2)])
print('20: ', [s2 for s2 in range(23, 1000) if not f(50, s2, 1) and f(50, s2, 3)])
print('21: ', [s2 for s2 in range(23, 1000) if not f(50, s2, 2) and f(50, s2, 4)])
