from itertools import permutations

k = 0
for x in permutations('01234', r=3):
    s = ''.join(x)

    if s[0] != '0' and int(s[0]) > int(s[1]) > int(s[2]):
        k += 1
print(k)

