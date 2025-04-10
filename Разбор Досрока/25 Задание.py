def findDel(num):
    delit = []
    for d in range(1, round(num ** 0.5)):
        if num % d == 0:
            delit.append(d)
            delit.append(num // d)

    return delit

c = 0
for num in range(1125000, 1300000):
    delit = findDel(num)

    f7 = [x for x in delit if x % 10 == 7 and x != 7]
    if len(f7) > 0 and c < 10:
        c += 1
        print(num, min(f7))