def deliteli(num):
    d = []
    for delit in range(2, round(num ** 0.5)):
        if num % delit == 0:
            d.append(delit)
            d.append(num // delit)
    return d


c = 0
for num in range(850_001, 900_000):
    dl = deliteli(num)
    F = max(dl) - min(dl) if len(dl) > 0 else 0

    if F != 0 and F % 5 == 0 and c < 6:
        print(num, F)
        c += 1