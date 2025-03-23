def semerka(N):
    new = ''
    while N > 0:
        new += str(N % 7)
        N //= 7
    return new[::-1]


res = []
for N in range(1, 100000):
    sem = semerka(N)

    if sem.count('2') % 2 == 0:
        sem += '555'
    else:
        sem = '1' + sem

    R = int(sem, 7)
    if R < 3799:
        res.append(N)
print(max(res))