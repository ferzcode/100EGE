def F(x, y):
    if x == y: return 1
    elif x > y or x == 35: return 0
    else: return F(x + 1, y) + F(x + 2, y) + F(x * 2, y)

print(F(7, 13) * F(13, 15) * F(15, 51))