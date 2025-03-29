def chetire(N):
    new = ''
    while N > 0:
        new += str(N % 4)
        N //= 4
    return new[::-1]


res = []
for N in range(1, 1000, +2):
    ch = chetire(N)

    if N % 3 == 0:
        ch = ch[-1] + ch[1:-1] + ch[0] + '1'
    else:
        ch += str(N % 3)

    R = int(ch, 4)
    if R <= 340:
        res.append(R)
print(max(res))