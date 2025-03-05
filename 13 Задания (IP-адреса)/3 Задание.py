from ipaddress import *

setochka = ip_network(f'252.67.33.87/255.252.0.0', False)

k = 0
for ip in setochka:
    dvoich = bin(int(ip))[2:]

    levie = dvoich[:16] # 0 - 15
    right = dvoich[16:] # 16 - 31

    if levie.count('1') * 2 < right.count('1'):
        k += 1
print(k)