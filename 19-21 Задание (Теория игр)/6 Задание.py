def f(s1, s2, m):
    if s1 + s2 <= 72: return m % 2 == 0
    if m == 0: return 0


    h = [f(s1 - 3, s2, m - 1), f(s1, s2 - 3, m - 1), f(s1 // 2 + 1, s2, m - 1), f(s1, s2 // 2 + 1, m - 1)]

    return any(h) if m % 2 != 0 else all(h)

# П В П В
# 1 2 3 4

print('19: ', [s2 for s2 in range(23, 1000) if f(50, s2, 2)])
print('20: ', [s2 for s2 in range(23, 1000) if not f(50, s2, 1) and f(50, s2, 3)])
print('21: ', [s2 for s2 in range(23, 1000) if not f(50, s2, 2) and f(50, s2, 4)])


