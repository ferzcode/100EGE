k = 0
for stroka in open('9 Задание.txt'):
    s = [int(x) for x in stroka.split()]
    triple = [x for x in s if s.count(x) == 3]  # 3
    ostalnie = [x for x in s if s.count(x) == 1]  # 3

    if len(triple) == 3 and len(ostalnie) == 3:
        if sum(triple) ** 2 > sum(ostalnie) ** 2:
            k += 1

print(k)
