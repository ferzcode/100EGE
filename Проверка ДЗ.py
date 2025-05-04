def treug(n, m, k):
    return n + m > k and m + k > n and k + n > m


def f(x):
    return (treug(A, 5, x) <= ((max(x, 11) <= 19) == (not treug(23, 13, x))))


for A in range(1, 1000):
    if all(f(x) == 1 for x in range(1, 1000)):
        print(A)
