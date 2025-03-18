def proverka(n, m, k):
    return (10 <= n <= 99) + (10 <= m <= 99) + (10 <= k <= 99)


m = [int(x) for x in open('17var05.txt')]
res = []

minik = [x for x in m if x % 100 == 25]

for i in range(len(m) - 2):
    summa = m[i] + m[i + 1] + m[i + 2]

    if proverka(m[i], m[i+1], m[i+2]) == 1 and summa < min(minik):
        res.append(summa)
print(len(res), max(res))