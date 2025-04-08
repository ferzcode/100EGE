f = open('4 Задание.txt').readline()

cFSQR = 0
maxln = 0
l = 0

for r in range(3, len(f)):
    if f[r - 3] + f[r - 2] + f[r - 1] + f[r] == 'FSRQ':
        cFSQR += 1

    while cFSQR > 80:
        if f[l] + f[l + 1] + f[l + 2] + f[l + 3] == 'FSRQ':
            cFSQR -= 1
        l += 1

    if cFSQR == 80:
        maxln = max(maxln, r - l + 1)
print(maxln)
