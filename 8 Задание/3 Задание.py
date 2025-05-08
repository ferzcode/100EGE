from itertools import *

nomer = 0
for x in product(sorted('ПОБЕДА'), repeat=6):
    s = ''.join(x)
    nomer += 1

    if nomer % 2 == 0 and s[0] == 'О' and len(set(s)) == len(s):
        print(nomer)