from ipaddress import *

for A in range(0, 256):
    setochka = ip_network(f'217.109.{A}.94/255.255.254.0', False)

    c = 0
    for ip in setochka:
        dvoyka = bin(int(ip))[2:].zfill(32)
        levie = dvoyka[:16]
        right = dvoyka[16:]

        if levie.count('0') <= right.count('0'):
            c += 1

    if len(list(setochka)) == c:
        print(A)
