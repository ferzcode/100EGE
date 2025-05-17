a = [0] * 21000

for i in range(6):
    a[i] = i

for i in range(6, 21000):
    a[i] = (3 * i - 2) * a[i - 5]

print((a[20568] - 51702 * a[20563])//a[20553])