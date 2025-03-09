from ipaddress import *

setochka = ip_network(f'172.16.192.0/255.255.192.0', False)
k = 0

for ip in setochka:
    dvoich = f'{ip:b}'
    if dvoich.count('1') % 5 != 0:
        k += 1
print(k)