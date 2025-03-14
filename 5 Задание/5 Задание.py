def chetire(N):
    new = ''
    while N > 0:
        new = str(N % 4) + new
        N //= 4
    return new

otveti = []
for N in range(1, 1000):
    che = chetire(N)

    if N % 4 == 0:
        che += che[-2:]
        # che = che + che[-2] + che[-1]
    else:
        ostatok = chetire((N % 4) * 2)
        che += ostatok

    R = int(che, 4)
    if R < 261:
        otveti.append(N)
print(max(otveti))