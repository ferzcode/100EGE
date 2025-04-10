def f(s, m):
    if s <= 87: return m % 2 == 0
    if m == 0: return 0

    h = [f(s - 2, m - 1), f(s // 2, m - 1)]
    return any(h) if m % 2 != 0 else all(h)
# 1 2 3 4
# П В П В

print('19: ', [s for s in range(88, 1000) if not f(s, 1) and f(s, 2)])
print('20: ', [s for s in range(88, 1000) if not f(s, 1) and f(s, 3)])
print('19: ', [s for s in range(88, 1000) if not f(s, 2) and f(s, 4)])