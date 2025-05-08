from itertools import *

nomer = 0
for x in product(sorted('ЛАЙМ'), repeat=5):
    s = ''.join(x)
    nomer += 1

    if s.count('М') == 0 and s.count('Л') == 0 and 'ЙЙ' not in s:
        print(nomer)