from ipaddress import ip_network

setka = ip_network('142.108.56.118/255.255.255.240', False)

count = 0
for ip in setka:
    # Левый байт - первые 16 бит
    # Правый байт - вторые 16 бит

    dvach = bin(int(ip))[2:]

    left = dvach[:16]
    right = dvach[16:]
    if left.count('1') < right.count('1'):
        count += 1

print(count)


