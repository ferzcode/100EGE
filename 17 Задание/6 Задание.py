from math import sqrt

def proverka(n):
    if n > 0:
        return int(n ** 0.5) ** 2 == n
    else:
        return False

m = [int(x) for x in open('17var13.txt')]
res = []

for i in range(len(m) - 1):
    if proverka(m[i]) or proverka(m[i + 1]):
        res.append(m[i] + m[i + 1])

print(len(res), max(res))

