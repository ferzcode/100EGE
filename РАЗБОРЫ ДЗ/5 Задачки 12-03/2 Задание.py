res = []
for N in range(1, 1000):
    binary = bin(N)[2:]

    if binary.count('0') % 2 == 0:
        binary = '1' + binary + '1'
    else:
        binary = '10' + binary

    R = int(binary, 2)
    if R < 100:
        res.append(R)
print(max(res))
