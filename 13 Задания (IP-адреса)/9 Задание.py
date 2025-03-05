from ipaddress import *

for A in range(0, 255):
    setochka = ip_network(f'192.214.{A}.184/255.255.255.224', False)

    c = 0
    for ip in setochka:
        dvoyka = bin(int(ip))[2:]

        if dvoyka.count('1') > 15:
            c += 1

    if c == len(list(setochka)):
        print(A)