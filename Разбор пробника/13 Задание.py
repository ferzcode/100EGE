from ipaddress import *

for A in range(0, 256):
    setochka = ip_network(f'126.255.{A}.100/255.255.240.0', False)

    c = 0
    for ip in setochka:
        binary = bin(int(ip))[2:].zfill(32)
        print(binary)
        if binary[:16].count('1') >= binary[16:].count('1'):
            c += 1

    # if c == len(list(setochka)):
    #     print(A)