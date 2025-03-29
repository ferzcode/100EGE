res = []
for N in range(100, 1000):
    s = str(N)

    proizv = int(s[0]) * int(s[1]) * int(s[2])
    summa  = int(s[0]) + int(s[1]) + int(s[2])

    R = str(max(proizv, summa)) + str(min(proizv, summa))

    if R == '24019':
        res.append(N)
print(max(res))


