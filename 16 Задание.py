# all() - ЕСЛИ ВСЕ / ДЛЯ ВСЕХ
# any() - ЕСЛИ ХОТЯ БЫ ОДИН
#
# КЛАССЫ ЧИСЕЛ
#
# НАТУРАЛЬНЫЕ - 1, 2, 3, .... +БЕСКОНЕЧНОСТЬ
# ЦЕЛЫЕ - -БЕСКОНЕЧНОСТЬ, ..., -1, 0, 1, 2, .... +БЕСКОНЕЧНОСТЬ
#
# 0
#
# ЦЕЛЫЕ ПОЛОЖИТЕЛЬНЫЕ - 1, 2, 3, .... +БЕСКОНЕЧНОСТЬ
# ЦЕЛЫЕ ОТРИЦАТЕЛЬНЫЕ - -БЕСКОНЕЧНОСТЬ, ..., -1
# ЦЕЛЫЕ НЕПОЛОЖИТЕЛЬНЫЕ - -БЕСКОНЕЧНОСТЬ, ..., -1, 0
# ЦЕЛЫЕ НЕОТРИЦАТЕЛЬНЫЕ - 0, 1, 2, ... +БЕСКОНЕЧНОСТИ

# 1 ПРОТОТИП - ФУНКЦИИ X и Y

# def f(x, y):
#     return (5 < y) or (x > 32) or (x + 2 * y < A)
#
# for A in range(0, 10000):
#     if all(f(x, y) == 1 for x in range(0, 10000) for y in range(0, 10000)):
#         print(A)

# 2 ПРОТОТИП - КОНЪЮНКЦИИ (&)
#
# def f(x):
#     return ((x & A != 0) <= ((x & 698 == 0) <= (x & 321 != 0)))
#
# for A in range(1, 10000):
#     if all(f(x) == 1 for x in range(1, 10000)):
#         print(A)

# 3 ПРОТОТИП - ДЕЛИТЕЛИ
#
# def f(x):
#     return (((x % 7 != 0) and (x % 13 == 0)) <= (x > A - 40))
#
# for A in range(1, 10000):
#     if all(f(x) == 1 for x in range(1, 10000)):
#         print(A)

# 4 ПРОТОТИП - ОТРЕЗКИ

# def f(x):
#     C = 48 <= x <= 94
#     J = 83 <= x <= 100
#     A = a1 <= x <= a2
#
#     return ((not (C or J)) <= (not A))
#
#
# r = []
# d = [y for x in [48, 94, 83, 100] for y in [x, x - 0.1, x + 0.1]] # точки для x
#
# for a1 in d:
#     for a2 in d:
#         if a2 >= a1 and all(f(x) == 1 for x in d): # f(x) == 0 если ложно
#             r += [a2 - a1]
#
# print(round(max(r))) # min / max в засимости от условия


# def f(x):
#     B = 36 <= x <= 75
#     C = 60 <= x <= 110
#     A = a1 <= x <= a2
#
#     return ((not A) <= (B == C))
#
#
# r = []
# d = [y for x in [36, 75, 60, 110] for y in [x - 0.1, x, x + 0.1]]
#
# for a1 in d:
#     for a2 in d:
#         if a2 >= a1 and all(f(x) == 1 for x in d):
#             r += [a2 - a1]
# print(round(min(r)))


def triug(n, m, k):
    return n + m > k or n + k > m or m + k > n


def f(x):
    return (triug(A, 7, x) <= (((max(x + 5, 14)) <= 27) == (not (triug(36, 21, x)))))


for A in range(1, 100000):
    if all(f(x) == 1 for x in range(1, 100000)):
        print(A)
