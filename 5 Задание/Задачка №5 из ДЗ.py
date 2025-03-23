def chetire(N):
    new = ''
    while N > 0:
        new += str(N % 4)
        N //= 4
    return new[::-1]


res = []
for N in range(1, 1000, +2):
    chet = chetire(N)

    if N % 3 == 0:
        chet = chet[-1] + chet[1:-1] + chet[0] + '1'
    else:
        chet = chet + str(N % 3)

    R = int(chet, 4)
    if R <= 340:
        res.append(R)
print(max(res))