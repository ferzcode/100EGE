for x in range(1, 2006):
    num = 43 ** 56 + 113 ** 841 - x

    # До 10 системы счисления - СТРОКУ
    new = ''
    while num > 0:
        new += str(num % 4)
        num //= 4
    new = new[::-1]

    # 0123
    if (new.count('0') + new.count('2')) % 2 == 0 and (new.count('1') + new.count('3')) % 2 == 0 and new.count('2') <= 712:
        print(x)