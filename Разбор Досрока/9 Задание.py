f = open('9 Задание.txt')

c = 0
for s in f:
    stroka = [int(x) for x in s.split()]

    p3 = [int(x) for x in stroka if stroka.count(x) == 3]
    np = [int(x) for x in stroka if stroka.count(x) == 1]

    if len(p3) > 0 and len(np) > 0:
        if len(p3) == 6 and len(np) == 1 and (max(p3) > np[0]):
            c += 1
print(c)
