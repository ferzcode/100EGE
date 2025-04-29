def troich(N):
    new = ''
    while N > 0:
        new += str(N % 3)
        N //= 3
    return new[::-1]

res = []
for N in range(3, 100000):
    tri = troich(N)
    if N % 3 == 0:
        tri = tri + tri[-2] + tri[-1]
    else:
        ostatok = troich((N % 3) * 3)
        tri += ostatok

    R = int(tri, 3)
    if R <= 150:
        res.append(N)
print(max(res))