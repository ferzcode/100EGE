def finddel(num):
    d = []
    for delit in range(2, round(num ** 0.5) + 1):
        if num % delit == 0 and delit != 9:
            d.append(delit)
            d.append(num // delit)
    return d


c = 0
for num in range(800_000, 1000_000):
    deliteli = finddel(num)

    d9 = [d for d in deliteli if d % 10 == 9]
    if len(d9) > 0 and c != 5:
        print(num, min(d9))
        c += 1