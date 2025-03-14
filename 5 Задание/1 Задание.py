otveti = []
for N in range(4, 1000):
    binary = bin(N)[2:]

    if N % 2 == 0:
        binary = binary + binary[0] + binary[1] + binary[2]
        # binary += binary[:3]
    else:
        binary = '1' + binary + '01'

    R = int(binary, 2)
    if R > 600:
        otveti.append(R)

print(min(otveti))