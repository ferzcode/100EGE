def F(x, A):
    return (x % A == 0) or ((200 <= x <= 300) <= (x % 77 != 0))

for A in range(1000, 0, -2):
    if all(F(x, A) == 1 for x in range(1, 1000)):
        print(A)
        break