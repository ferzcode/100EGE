from itertools import product

nomer = 0
count = 0
for kombo in product(sorted("ФАВОРИТ"), repeat=6):
    nomer += 1
    s = ''.join(kombo)

    if s[0] != 'О' and s.count('Р') == 2 and nomer % 2 == 0:
        count += 1
print(count)

