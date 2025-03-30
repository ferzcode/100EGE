def F(x, A):
    return ((x % A != 0) <= ((x % 26 == 0) <= (x % 169 != 0)))

for A in range(1, 10000):
    if all(F(x, A) == 1 for x in range(1, 1000)):
        print(A)