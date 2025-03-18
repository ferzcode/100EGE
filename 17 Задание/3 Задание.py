m = [int(x) for x in open('17_17558.txt')]
res = []
kr32 = [i for i in m if abs(i) % 32 == 0]

for i in range(len(m) - 1):
    if (m[i] < 0 or m[i + 1] < 0) and (m[i] + m[i + 1]) < len(kr32):
        res.append(m[i] + m[i + 1])

print(len(res), max(res))