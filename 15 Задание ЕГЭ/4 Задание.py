def triangle(n, m, k):
    return (n + m + k - max(n, m, k)) > max(n, m, k) # Неравенство треугольника
    # return (n + m) > k and (n + k) > m and (m + k) > n # Неравенство треугольника

def F(x, A):
    return not((triangle(x, 12, 20) == (not((max(x, 5) > 28)))) and triangle(x, A, 3))

for A in range(1000, 0, -1):
    if all(F(x, A) == 1 for x in range(1, 1000)):
        print(A)
        break