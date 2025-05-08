from itertools import *

nomer = 0
for x in product(sorted('КОДИМ'), repeat=5):
    s = ''.join(x)
    nomer += 1

    if s.count('М') == 2 and 'ММ' not in s:
        print(nomer)
