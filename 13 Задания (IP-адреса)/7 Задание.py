from ipaddress import *

k = 0
for A in range(0, 256):
    setochka = ip_network(f'127.254.{A}.10/255.255.224.0', False)

    count = 0
    for ip in setochka:
        dvoich = bin(int(ip))[2:].zfill(32)

        levie = dvoich[:16] # 0- 15
        pravie = dvoich[16:] # 16 - 31

        if levie.count('1') >= pravie.count('1'):
            count += 1

    if count == len(list(setochka)):
        print(A)
