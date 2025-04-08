f = open('1 Задание.txt').readline()

maxln = 0
c = 1

for i in range(len(f) - 1):
    if int(f[i]) % 2 != int(f[i + 1]) % 2:
        c += 1
    else:
        maxln = max(maxln, c)
        c = 1

print(maxln)