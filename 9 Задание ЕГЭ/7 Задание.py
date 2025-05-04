c = 0

for stroka in open('7 Задание.txt'):
    s = [int(x) for x in stroka.split()]

    povtorvki = [num for num in s if s.count(num) == 3]
    np = [num for num in s if s.count(num) == 1]

    if len(np) > 0 and len(povtorvki) > 0:
        if len(povtorvki) == 6 and len(np) == 1 and max(povtorvki) > np[0]:
            c += 1
print(c)
