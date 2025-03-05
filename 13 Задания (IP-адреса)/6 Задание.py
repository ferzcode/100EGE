from ipaddress import *

for mask in range(0, 33):

    setochka = ip_network(f'44.44.229.28/{mask}', False)

    if '44.44.224.0' in str(setochka):
        print(mask)
