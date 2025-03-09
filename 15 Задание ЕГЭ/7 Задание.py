def F(x, y, A):
    return (3 * x + y > 48) or (x > y) or (4 * x + y < A)

for A in range(1000, -1000, -1):
    if any(F(x, y, A) == 0 for x in range(0, 100) for y in range(0, 100)):
        print(A)
        break
