from ipaddress import*

counter_A = 0
for A in range(0, 256):
    setka = ip_network(f'207.0.{A}.167/255.255.255.192', False)

    k = 0
    for ip in setka:
        dvoich = bin(int(ip)).zfill(32)[2:]
        left = dvoich[:16]
        right = dvoich[16:]

        if left.count('0') > right.count('0'):
            k += 1
    if k == len(list(setka)):
        counter_A += 1
print(counter_A)
