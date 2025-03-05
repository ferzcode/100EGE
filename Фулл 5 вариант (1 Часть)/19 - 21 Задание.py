# П В П В
# 1 2 3 4

def f(s1, m):
    if s1 >= 202: return m % 2 == 0
    if m == 0: return 0
    h = [f(s1 + 1, m - 1), f(s1 + 4, m - 1), f(s1 * 3, m - 1)]
    return any(h) if m % 2 != 0 else all(h)

print('19)', [s1 for s1 in range(1, 202) if f(s1, 2)])
print('20)', [s1 for s1 in range(1, 202) if not (f(s1, 1)) and f(s1, 3)])
print('21)', [s1 for s1 in range(1, 202) if not f(s1, 2) and f(s1, 4)])
