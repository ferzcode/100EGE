def F(x, y):
    return (5 < y) or (x > 32) or (x + 2 * y < A)

for A in range(0, 1000):
    if all(F(x, y) == 1 for x in range(0, 1000) for y in range(0, 1000)):
        print(A)