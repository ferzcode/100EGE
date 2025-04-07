
def F(x, A):
    return ((x % 13 == 0) <= (x % 21 != 0)) or (x + A >= 500)

for A in range(1, 10000):
    if all(F(x, A) == 1 for x in range(1, 1000)):
        print(A)
        