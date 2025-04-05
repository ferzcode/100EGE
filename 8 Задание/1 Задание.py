from itertools import *

nomer = 0
for x in product(sorted('ЯНВАРЬ'), repeat=5):
    nomer += 1
    s = ''.join(x)

    if s[0] != 'Я' and s.count('Ь') <= 1 and 'ЯЯ' not in s:
        print(nomer)