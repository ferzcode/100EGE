def pyterka(N):
    new = ''
    while N > 0:
        new += str(N % 5)
        N //= 5
    return new[::-1]


res = []
for N in range(1, 100000):
    pyat = pyterka(N)

    if N % 2 == 0:
        ml = int(pyat[-1], 5)
        ml = pyterka(ml * 3)
        pyat += ml
    else:
        pyat = pyat[-1] + pyat[1:-1] + pyat[0] + '1'

    R = pyterka(int(pyat, 5))

    if R.count('0') == 4:
        res.append(N)
print(min(res))
