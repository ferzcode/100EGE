# from itertools import permutations
import re


def prime(n):
    count = 0
    for delit in range(2, round(n ** 0.5)):
        if n % delit == 0:
            count += 2

    return True if count == 0 else False


for n in range(1, 1000):
    s = '>' + '0' * 15 + '1' * n + '2' * 15

    while '>0' in s or '>1' in s or '>2' in s:
        if '>0' in s:
            s = s.replace('>0', '22>', 1)
        if '>1' in s:
            s = s.replace('>1', '2>', 1)
        if '>2' in s:
            s = s.replace('>2', '1>', 1)

    summa = s.count('2') * 2 + s.count('1') * 1

    if prime(summa):
        print(n)
        break
