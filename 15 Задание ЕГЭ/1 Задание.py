def F(x, A):
    return ((x % 9 == 0) <= (x % 6 != 0)) or (x + A >= 100)

for A in range(1, 1000):
    if all(F(x, A) == 1 for x in range(1, 1000)):
        print(A)
        break