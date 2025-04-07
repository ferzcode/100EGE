def F(x):
    return ((x & 52 != 0) and (x & 36 == 0)) <= (x & A != 0)


for A in range(0, 10000):
    if all(F(x) == 1 for x in range(1, 10000)):
        print(A)