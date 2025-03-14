def triple(N):
    new = ''
    while N > 0:
        new = str(N % 3) + new
        N //= 3
    return new

otveti = []
for N in range(1, 1000):
    tri = triple(N)

    summa = tri.count('2') * 2 + tri.count('1') * 1
    # summa = sum(map(int, tri))
    # summa = sum(int(x) for x in tri)

    if summa % 2 == 0:
        tri = '12' + tri[2:] + '0'
    else:
        tri = '10' + tri[2:] + '2'

    R = int(tri, 3)
    if R > 105:
        otveti.append(N)

print(min(otveti))




#        0123456
slovo = 'КАПИБАРА'
print(slovo[:len(slovo)//2])


# for (левая, правая)









