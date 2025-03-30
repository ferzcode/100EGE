m = [int(x) for x in open('17.txt')]
res = []
for i in range(len(m) - 1):
    if abs(m[i] % 10 == 7) and abs(m[i + 1] % 10 == 7):
        res.append(abs(m[i + 1] - m[i]))
print(len(res), min(res))
