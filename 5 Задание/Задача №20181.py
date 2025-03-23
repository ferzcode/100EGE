res = []
for N in range(1, 1000):
    binary = bin(N)[2:]

    if N % 2 == 0:
        kolvo_1 = binary.count('1')
        kolvo_1 = bin(kolvo_1)[2:]
        binary += kolvo_1
    else:
        binary = '1' + binary + '101'

    R = int(binary, 2)
    if R > 350:
        res.append(N)
print(min(res))