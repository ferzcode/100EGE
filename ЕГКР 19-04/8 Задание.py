from itertools import *

# product - МОЖЕТ ДЕЛАТЬ ПОВТОРЯЮЩИЕ СИМВОЛЫ
# permutations - ВСЕ СИМВОЛЫ РАЗЛИЧНЫЕ

nomer = 0
for i in product(sorted('ПОБЕДА'), repeat=6):
    s = ''.join(i)
    nomer += 1

    if s[0] == 'О' and len(set(s)) == len(s) and nomer % 2 == 0:
        print(nomer)