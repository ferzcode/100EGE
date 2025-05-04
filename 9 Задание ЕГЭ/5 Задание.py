
c = 0
for stroka in open('5 Задание.txt'):
    s = [int(x) for x in stroka.split()]

    # s.sort() # От меньшего к большему
    a = sorted(s) # От меньшего к большему

    if len(s) == len(set(s)) and (a[3] + a[4]) <= (a[2] + a[1] + a[0]):
        c += 1
print(c)

