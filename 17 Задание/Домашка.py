def f(n, m):
    ln = n % 10
    lm = m % 10
    return (ln % 2 != 0) + (lm % 2 != 0) + (ln == lm)


m = [int(x) for x in open('C:/Users/and18/Downloads/Telegram Desktop/17/17var19.txt')]
res = []
for i in range(len(m) - 1):
    if f(m[i], m[i + 1]):
        res.append(m[i] * m[i + 1])
print(len(res), max(res))
