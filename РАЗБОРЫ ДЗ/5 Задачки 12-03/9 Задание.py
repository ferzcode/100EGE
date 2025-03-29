def troich(N):
    new = ''
    while N > 0:
        new += str(N % 3)
        N //= 3
    return new[::-1]

res = []
for N in range(1, 1000):
    tri = troich(N)

    if N % 3 == 0:
        tri = '1' + tri + '02'
    else:
        ostatok = troich((N % 3) * 4)
        tri += ostatok
    R = int(tri, 3)
    if R < 199:
        res.append(N)
print(max(res))