f = open('2 Задание.txt').readline()

maxln = 0
c = 1

for i in range(len(f) - 1):
    if (f[i].isalpha() and f[i + 1].isdigit()) or (f[i].isdigit() and f[i + 1].isalpha()):
        c += 1
    else:
        maxln = max(maxln, c)
        c = 1

print(maxln)