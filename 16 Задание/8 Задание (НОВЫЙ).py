a = [0] * 2100

for i in range(2010, 2100):
    a[i] = i

for i in range(2009, 0, -1):
    a[i] = a[i + 3] + a[i + 2] + a[i + 1]

print((a[2000] - 2 * (a[2002] + a[2003]))//a[2004])