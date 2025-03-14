for N in range(100, 1000):
    chislo = str(N)

    perv = int(chislo[0])
    vtor = int(chislo[1])
    tret = int(chislo[2])

    summa1 = perv ** 2 + vtor ** 2
    summa2 = vtor ** 2 + tret ** 2

    res = str(max(summa1, summa2)) + str(min(summa1, summa2))

    if res == '9752':
        print(N)


