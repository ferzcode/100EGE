res =[]
for N in range(1, 1000):
    binary = bin(N)[2:]

    if sum(map(int, binary)) % 2 == 0:
        binary = '10' + binary[2:] + '0'
    else:
        binary = '11' + binary[2:] + '1'

    R = int(binary, 2)
    if R > 19:
        res.append(N)
print(min(res))