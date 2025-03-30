k = 0
for s in open('9 Задание.txt'):
    stroka = [int(x) for x in s.split()]

    povtor4 = [int(x) for x in stroka if stroka.count(x) == 4] # len == 4
    povtor2 = [int(x) for x in stroka if stroka.count(x) == 2] # len == 2
    povtor1 = [int(x) for x in stroka if stroka.count(x) == 1] # len == 2

    maxi = max(povtor4 + povtor2) if len(povtor2) > 0 and len(povtor4) > 0 else None
    if len(povtor4) == 4 and len(povtor2) == 2 and len(povtor1) == 2 \
        and sum(povtor1) / len(povtor1) >= maxi:
        k += 1
print(k)

