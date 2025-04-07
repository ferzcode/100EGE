def F(x, y):
    return (3 * x + y > 48) or (x > y) or (4 * x + y < A)

for A in range(-10000, 10000):
    if any(F(x, y) == 0 for x in range(0, 1000) for y in range(0, 1000)):
        print(A)