res = []
for N in range(1, 100000):
    N -= N % 4

    binary = bin(N)[2:]
    summa = sum(map(int, binary))
    binary += str(summa % 2)
    summa = sum(map(int, binary))
    binary += str(summa % 2)

    R = int(binary, 2)
    if R < 47:
        res.append(N)

print(max(res))

