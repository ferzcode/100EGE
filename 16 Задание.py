from itertools import *

nomer = 0
for x in product(sorted(set('СУБЛИМАЦИЯ')), repeat=5):
    nomer += 1
    s = ''.join(x)

    # ГЛАСНЫЕ - УИАЯ
    if nomer % 2 != 0 and s[-1] != 'Я' and (s.count('У') + s.count('И') + s.count('А') + s.count('Я')) == 2:
        print(nomer)