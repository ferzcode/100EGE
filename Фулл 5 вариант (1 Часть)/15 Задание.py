def F(x, y, A):
    return (4 * x + y < A) or (x < y) or (22 <= x)


for A in range(-300, 1000):
    if all(F(x, y, A) == 1 for x in range(0, 1000) for y in range(0, 1000)):
        print(A)
        break
