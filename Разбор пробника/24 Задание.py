f = open('24 Задание.txt').readline()

maxi = 0
c = 1
for i in range(0, len(f) - 1):
    if f[i] >= f[i + 1]:
        c += 1
    else:
        maxi = max(c, maxi)
        c = 1
print(maxi)
