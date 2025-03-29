res = []
for N in range(1, 13):
    binary = bin(N)[2:]

    if N % 2 == 0:
        binary = '10' + binary
    else:
        binary = '1' + binary + '01'

    R = int(binary, 2)
    res.append(R)
print(max(res))