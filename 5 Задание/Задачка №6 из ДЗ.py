def chetire(N):
    new = ''
    while N > 0:
        new += str(N % 4)
        N //= 4
    return new[::-1]


res = []
for N in range(1, 1000):
    chet = chetire(N)

    if len(chet) % 2 == 0:
        chet = chet[:len(chet) // 2] + '0' + chet[len(chet) // 2:]

    R = int(chet)
    if R <= 180:
        res.append(N)
print(max(res))
