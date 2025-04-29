nomer = 0
for s in open('9.txt'):
    stroka = [int(x) for x in s.split()]
    nomer += 1

    # if stroka[0] > stroka[1] > stroka[2] > stroka[3] > stroka[4] > stroka[5] > stroka[6]:
    if stroka == sorted(stroka, reverse=True):
        if (min(stroka) + max(stroka)) / 2 > (sum(stroka) - min(stroka) - max(stroka)) / 5:
            print(nomer)
            break

