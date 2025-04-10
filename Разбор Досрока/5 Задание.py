res = []

for N in range(1, 100000):
    binary = bin(N)[2:]

    # summa = sum(map(int, binary))
    summa = binary.count('1')
    if summa % 2 == 0:
        binary = '10' + binary[2:] + '0'
    else:
        binary = '11' + binary[2:] + '1'

    R = int(binary, 2)
    if R > 480:
        res.append(N)
print(min(res))