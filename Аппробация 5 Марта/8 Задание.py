from itertools import *

mesto = 0
for combo in product(sorted('ФОКУС'), repeat=5):
    mesto += 1
    s = ''.join(combo)

    if s.count('Ф') == 0 and s.count('У') == 2:
        print(mesto)