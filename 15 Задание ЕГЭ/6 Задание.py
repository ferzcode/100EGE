def f(x, A):
    return (x % A == 0) or ((60 <= x <= 80) <= (x % 22 != 0))

for A in range(1000, 0, -1):
    if all(f(x, A) == 1 for x in range(1, 1000)):
        print(A)
        break

