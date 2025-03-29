def troich(N):
    new = ''
    while N > 0:
        new += str(N % 3)
        N //= 3
    return new[::-1]

res = []
for N in range(1, 1000):
    tri = troich(N)
    if sum(map(int, tri)) % 2 == 0:
        tri = '1' + tri + '2'
    else:
        tri = '2' + tri + '0'

    R = int(tri, 3)
    if R > 100:
        res.append(R)
print(min(res))


