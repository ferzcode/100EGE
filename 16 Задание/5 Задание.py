def F(x, y):
    if x == y: return 1
    elif x < y or x == 24: return 0
    else: return F(x - 1, y) + F(x - 6, y) + F(x // 2, y)

print(F(34, 29) * F(29, 19) * F(19, 6))