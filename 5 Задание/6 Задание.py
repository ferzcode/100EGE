otveti = []

for N in range(1, 1000):
    binary = bin(N)[2:]

    if N % 2 == 0:
        binary += '0'
    else:
        binary += '1'

    if binary.count('1') % 3 == 0:
        binary = '11' + binary[2:]
    else:
        binary = '10' + binary[2:]

    R = int(binary, 2)
    if R <= 37:
        otveti.append(N)
print(max(otveti))