res = []
for N in range(1, 100000):
    N = N - N % 4
    binary = bin(N)[2:]

    summa = binary.count('1') % 2
    binary += str(summa)
    summa = binary.count('1') % 2
    binary += str(summa)

    R = int(binary, 2)
    if R > 100:
        res.append(R)
print(min(res))