otveti = []

for N in range(1, 1000):
    binary = bin(N)[2:]

    if N % 4 == 0:
        binary = binary + binary
    else:
        binary = binary + binary[::-1]

    R = int(binary, 2)
    if R >= 544:
        otveti.append(N)
print(min(otveti))