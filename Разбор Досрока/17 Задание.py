f = open('17_21416.txt')
a = [int(x) for x in f]

summa = sum([x for x in a if x < 0])

res = []
for i in range(len(a) - 2):
    if (max(a[i], a[i + 1], a[i + 2]) * min(a[i], a[i + 1], a[i + 2])) > summa:
        res.append((a[i] + a[i + 1] + a[i + 2]))

print(len(res), max(res))
