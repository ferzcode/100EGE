otveti = []
for N in range(1, 1000):
    binary = bin(N)[2:]

    if N % 2 == 0:
        binary = binary.replace('1', '11')
    else:
        binary = binary.replace('0', '00')
    R = int(binary, 2)

    if R > 70:
        otveti.append(N)
print(min(otveti))
