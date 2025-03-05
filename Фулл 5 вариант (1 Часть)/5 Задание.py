def chetverki(N):
    new = ''
    while N > 0:
        new += str(N % 4)
        N //= 4
    return new[::-1]

ar = []
for N in range(1, 10000):
    chetire = chetverki(N)

    if N % 4 == 0:
        chetire = chetire + chetire[-2] + chetire[-1]
    else:
        ostatok = chetverki((N % 4) * 2)
        chetire += ostatok

    R = int(chetire, 4)
    if R < 261:
        ar.append(N)

print(max(ar))