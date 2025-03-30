def F(x, y):
    if x < y: return 0
    elif x == y: return 1
    else: return F(x - 1, y) + F(x // 2, y)

print(F(31, 12) * F(12, 2))