from ipaddress import *

setochka = ip_network(f'142.108.56.118/255.255.255.240', False)

k = 0
for ip in setochka:
    dvoich = bin(int(ip))[2:].zfill(32)

    levie = dvoich[:16] # 0 - 15
    pravie = dvoich[16:] # 16 - 31

    if levie.count('1') < pravie.count('1'):
        k += 1
print(k)