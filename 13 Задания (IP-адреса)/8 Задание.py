from ipaddress import *

for A in range(255, -1, -1):
    setochka = ip_network(f'126.255.{A}.100/255.255.240.0', False)

    k = 0
    for ip in setochka:
        dvoyka = bin(int(ip))[2:]

        levie = dvoyka[:16]
        right = dvoyka[16:]

        if levie.count('1') >= right.count('1'):
            k += 1

    if len(list(setochka)) == k:
        print(A)