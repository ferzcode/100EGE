for N in range(100, 1000):
    chislo = str(N)

    perv = int(chislo[0])
    vtor = int(chislo[1])
    tret = int(chislo[2])

    proizv = perv * vtor * tret
    summa = perv + vtor + tret

    res = str(max(proizv, summa)) + str(min(proizv, summa))
    if res == '33621':
        print(N)