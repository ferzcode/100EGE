def sem(N):
    new = ''
    while N > 0:
        new += str(N % 7)
        N //= 7
    return new[::-1]

res = []
for N in range(1, 100000):
    sm = sem(N)

    if sm.count('2') % 2 == 0:
        sm += '555'
    else:
        sm = '1' + sm

    R = int(sm, 7)
    if R < 3799:
        res.append(N)
print(max(res))