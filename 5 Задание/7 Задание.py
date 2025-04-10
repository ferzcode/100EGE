otveti = []

for N in range(1. 1000):
    binary = bin(N)[2:]
    seredina = len(binary) // 2

    if len(binary) % 2 == 0:
        binary = binary[:seredina] + '1' + binary[seredina:]

    R = int(binary, 2)
    if R <= 26:
        otveti.append(N)
print(max(otveti))