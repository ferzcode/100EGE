res = []
for N in range(1, 1000):
    binary = bin(N)[2:]

    if sum(map(int, binary)) % 2 == 0:
        binary = '101' + binary[3:] + '01'
    else:
        binary = '111' + binary[3:] + '10'

    R = int(binary, 2)
    if R < 385:
        res.append(N)
print(max(res))
