from ipaddress import *

for A in range(0, 256):
    setka = ip_network(f'126.255.{A}.100/255.255.240.0', False)
    K = 0
    for ip in setka:
        dvoich = bin(int(ip))[2:].zfill(32)
        left = dvoich[:16]
        right = dvoich[16:]

        if left.count('1') >= right.count('1'):
            K += 1
    if K == len(list(setka)):
        print(A)
