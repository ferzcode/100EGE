from ipaddress import *

setochka = ip_network(f'143.168.72.213/255.255.255.240', False)
for ip in setochka.hosts():
    print(ip)