from ipaddress import *

setochka = ip_network(f'204.16.168.0/255.255.248.0', False)

k = 0
for ip in setochka:
    dvoich = bin(int(ip))[2:]

    if dvoich.count('1') % 5 != 0:
        k += 1
print(k)