def proverka(n, m, k):
    return (100 <= n <= 999) + (100 <= m <= 999) + (100 <= k <= 999)


m = [int(x) for x in open('17var06.txt')]
res = []
k100 = [x for x in m if x % 1000 == 100]

for i in range(len(m) - 2):
    summa = m[i] + m[i + 1] + m[i + 2]
    if proverka(m[i], m[i + 1], m[i + 2]) == 2 and summa <= max(k100):
        res.append(summa)
print(len(res), max(res))
