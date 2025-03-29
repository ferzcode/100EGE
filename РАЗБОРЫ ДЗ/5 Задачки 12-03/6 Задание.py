def chetire(N):
    new = ''
    while N > 0:
        new += str(N % 4)
        N //= 4
    return new[::-1]


res = []
for N in range(1, 1000):
    ch = chetire(N)

    if len(ch) % 2 == 0:
        ch = ch[:len(ch) // 2] + '0' + ch[len(ch) // 2:]

    R = int(ch)
    if R <= 180:
        res.append(N)
print(max(res))