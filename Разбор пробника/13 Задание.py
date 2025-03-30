from ipaddress import *

for A in range(0, 256):
    set1 = ip_network(f'126.255.{A}.100/255.255.240.0', False)

    c = 0
    for ip in set1:
        dvoich = bin(int(ip))[2:].zfill(32)

        if dvoich[:16].count('1') >= dvoich[16:].count('1'):
            c += 1

    if c == len(list(set1)):
        print(A)
