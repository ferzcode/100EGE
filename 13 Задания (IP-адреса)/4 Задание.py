from ipaddress import *

A = [0, 128, 192, 224, 240, 248, 252, 254, 255]

for znach in A:
    setochka = ip_network(f'191.239.130.3/255.255.{znach}.0', False)

    k = 0
    for ip in setochka:
        dvoich = bin(int(ip))[2:].zfill(32)
        levie = dvoich[:16] # 0 - 15
        right = dvoich[16:] # 16 - 31

        if levie.count('1') >= right.count('1'):
            k += 1

    if k == len(list(setochka)):
        print(znach)
        break
