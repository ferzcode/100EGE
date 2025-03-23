def troich(N):
    new = ''
    while N > 0:
        new += str(N % 3)
        N //= 3
    return new[::-1]

res = []
for N in range(1, 1000):
    troyka = troich(N)
    summa = sum(map(int, troyka))

    if summa % 2 == 0:
        troyka = '1' + troyka + '2'
    else:
        troyka = '2' + troyka + '0'

    R = int(troyka, 3)
    if R > 100:
       res.append(R)
print(min(res))