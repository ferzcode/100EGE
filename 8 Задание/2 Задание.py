from itertools import *

count = 0
for x in permutations('01234567', r=5):
    s = ''.join(x)

    # Четные меняем на t 0246
    # Нечетные меняем на n 1357

    if s[0] != '0' and s.count('1') == 0:
        s = s.replace('0', 't')
        s = s.replace('2', 't')
        s = s.replace('4', 't')
        s = s.replace('6', 't')

        s = s.replace('3', 'n')
        s = s.replace('5', 'n')
        s = s.replace('7', 'n')

        if 'tt' not in s and 'nn' not in s:
            count += 1
print(count)
