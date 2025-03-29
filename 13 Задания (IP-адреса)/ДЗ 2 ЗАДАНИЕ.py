from ipaddress import *

# for mask in range(33):
#     set1 = ip_network(f'157..220.185.237/{mask}', False)
#     set2 = ip_network(f'157..220.184.230/{mask}', False)
#     if set1 == set2:
#         print(mask)

setochka = ip_network(f'157.220.185.237/23', False)
count = 0 # Счетчик подходях IP - адресов

for ip in setochka:
    dvoich = bin(int(ip))[2:].zfill(32)
    if dvoich.count('1') == 15:
        count += 1
print(count)
