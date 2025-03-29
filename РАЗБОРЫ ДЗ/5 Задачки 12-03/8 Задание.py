def troich(N):
    new = ''
    while N > 0:
        new += str(N % 3)
        N //= 3
    return new[::-1]

res = []
for N in range(1, 1000):
    tri = troich(N)

    if sum(map(int, tri)) %  3 == 0:
        tri = '20' + tri
    else:
        tri = '10' + tri

    R = int(tri, 3)
    if R < 100:
        res.append(N)
print(max(res))