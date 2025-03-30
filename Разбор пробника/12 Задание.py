def prime(N):
    c = 0
    for delit in range(2, round(N ** 0.5)):
        if N % delit == 0:
            c += 1

    return True if c == 0 else False


for n in range(1, 1000):
    s = '>' + '0' * 15 + '1' * n + '2' * 15

    while '>0' in s or '>1' in s or '>2' in s:
        if '>0' in s:
            s = s.replace('>0', '22>', 1)
        if '>1' in s:
            s = s.replace('>1', '2>', 1)
        if '>2' in s:
            s = s.replace('>2', '1>', 1)

    summa = s.count('1') + s.count('2') * 2
    if prime(summa):
        print(n)
        break