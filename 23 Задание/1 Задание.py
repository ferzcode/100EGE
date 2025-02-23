def F(x, y):
    if x == y: return 1
    elif x > y: return 0
    else: return F(x + 2, y) + F(x * 4, y)

print(F(3, 200) * F(200, 510))