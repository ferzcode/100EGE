from itertools import *

k = 0
for x in product('0123456', repeat=7):
    s = ''.join(x)

    if s[0] != '0' and s.count('0') + s.count('2') + s.count('4') + s.count('6') == 2:
        k += 1

print(k)