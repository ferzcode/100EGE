a = [0] * 3000

for i in range(2025, 3000):
    a[i] = i

for i in range(2024, 0, -1):
    a[i] = i * 2 + a[i + 2]

print(a)
print(a[82] - a[81])