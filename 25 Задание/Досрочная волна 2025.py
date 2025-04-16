def finddel(num):
    d = []
    for delit in range(2, round(num ** 0.5)):
        if num % delit == 0 and delit != 7:
            d.append(delit)
            d.append(num // delit)
    return d


c = 0
for num in range(1_125_000, 1300_000):
    deliteli = finddel(num)

    d7 = [d for d in deliteli if d % 10 == 7]
    if len(d7) > 0 and c != 5:
        print(num, min(d7))
        c += 1