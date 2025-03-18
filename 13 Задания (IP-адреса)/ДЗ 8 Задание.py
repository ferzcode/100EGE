from ipaddress import *

count_A = 0
for A in range(0, 256):
    setochka = ip_network(f'207.0.{A}.167/255.255.255.192', False)

    count = 0
    for ip in setochka:
        dvoich = bin(int(ip))[2:].zfill(32)

        if dvoich[0:16].count('0') > dvoich[16:].count('0'):
            count += 1

    if len(list(setochka)) == count:
        count_A += 1
print(count_A)

