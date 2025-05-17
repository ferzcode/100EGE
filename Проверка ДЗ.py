# a = [0] * 4000
#
# for i in range(0, 6):
#     a[i] = 1
#
# for i in range(6, 2127):
#     a[i] = i + a[i - 2]
#
# print(a[2126] - a[2122])

a = [0] * 21000

for i in range(6):
    a[i] = i

for i in range(6, 21000):
    a[i] = (3 * i - 2) * a[i - 5]

print((a[20568] - 51702 * a[20563])//a[20553])