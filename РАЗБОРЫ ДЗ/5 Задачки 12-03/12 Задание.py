def chetire(N):
    new = ''
    while N > 0:
        new += str(N % 4)
        N //= 4
    return new[::-1]

res = []
for N in range(1, 1000):
    ch = chetire(N)

    if N % 4 == 0:
        # ch += ch[-2:]
        ch = ch + ch[-2] + ch[-1]
    else:
        ostatok = chetire((N % 4) * 2)
        ch += ostatok

    R = int(ch, 4)
    if R >= 1025:
        res.append(N)
print(min(res))