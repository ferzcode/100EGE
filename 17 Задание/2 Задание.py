m = [int(x) for x in open('17_17873.txt')]
minik = min(m)

count = 0
maxi = 0

for i in range(len(m) - 1):
    if m[i] % 16 == minik or m[i + 1] % 16 == minik:
        count += 1
        maxi = max(maxi, m[i] + m[i + 1])

print(count, maxi)