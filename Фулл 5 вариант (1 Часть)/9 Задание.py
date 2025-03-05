count = 0
for s in open('9 Задание.txt'):
    stroka = [int(x) for x in s.split()]
    povtorki = [x for x in stroka if stroka.count(x) == 3] # 6 чисел
    raznie = [x for x in stroka if stroka.count(x) == 1] # 2 числа

    maxi = max(stroka)

    if len(povtorki) == 6 and len(raznie) == 2 and stroka.count(maxi) == 1:
        count += 1
        print(stroka)
print(count)


