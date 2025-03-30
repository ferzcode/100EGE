f = open('17 Задание.txt')
a = [int(x) for x in f]
c = 0
minik = 1000000000000000000000000

for i in range(len(a) - 1):
    if abs(a[i]) % 10 == 7 and abs(a[i + 1]) % 10 == 7:
        c += 1
        minik = min(abs(a[i] - a[i + 1]), minik)
print(c, minik)