from ipaddress import *

for A in range(0, 256):
    setochka = ip_network(f'32.0.{A}.5/255.255.240.0', False)

    k = 0
    for ip in setochka:
        dvoich = bin(int(ip))[2:].zfill(32)

        levie = dvoich[:16]
        pravie = dvoich[16:]

        if levie.count('1') <= pravie.count('1'):
            k += 1

    if k == len(list(setochka)):
        print(A)
        break