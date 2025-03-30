def F(s1, s2, m):
    if s1 + s2 >= 118: return m % 2 == 0
    if m == 0: return 0

    h = [F(s1 + 2, s2, m - 1), F(s1, s2 + 2, m - 1), F(s1 * 2, s2, m - 1), F(s1, s2 * 2, m - 1)]
    return any(h) if m % 2 != 0 else any(h)
# 1234
# ПВПВ

print('19: ', [s2 for s2 in range(1, 114) if F(3, s2, 2)])
print('20: ', [s2 for s2 in range(1, 114) if not F(3, s2, 1) and F(3, s2, 3)])
print('21: ', [s2 for s2 in range(1, 114) if not F(3, s2, 2) and F(3, s2, 4)])