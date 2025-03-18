from ipaddress import *

maski_A = [0, 128, 192, 224, 240, 248, 252, 254, 255]

for A in maski_A:
    setochka = ip_network(f'187.124.21.237/255.255.{A}.0', False)
    count = 0

    for ip in setochka:
        boba = bin(int(ip))[2:].zfill(32)

        levie = boba[:16]
        right = boba[16:]
        if levie.count('1') >= right.count('1'):
            count += 1

    if count == len(list(setochka)):
        print(A)