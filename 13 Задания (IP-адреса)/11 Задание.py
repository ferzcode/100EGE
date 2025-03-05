from ipaddress import *

# 0 1 2 3 4 5 6 7         - индексы первого байта
# 89 10 11 12 13 14 15    - индексы второго байта
# 16 17 18 19 20 21 22 23 - индексы третьего байта
# 24 25 26 27 28 29 30 31 - индексы четвертого байта

k = 0
for A in range(0, 256):
    net = ip_network(f'246.81.65.{A}/27', False)
    spisok_uzlov = list(net.hosts())

    c = 0
    for uzel in spisok_uzlov:
        dvoyka = bin(int(uzel))[2:].zfill(32)

        if dvoyka[16:24].count('0') > dvoyka[24:].count('0'):
            c += 1

    if c == len(spisok_uzlov):
        k += 1

print(k)
