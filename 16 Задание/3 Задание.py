def F(n):
    if n == 3:
        return 1
    if n > 3:
        return 5 * F(n - 1) + 6 * G(n - 1) - 3 * n + 8

def G(n):
    if n == 3:
        return 1
    if n > 3:
        return 6 * F(n - 1) + 5 * G(n - 1) + 3

print(F(9) + G(9))