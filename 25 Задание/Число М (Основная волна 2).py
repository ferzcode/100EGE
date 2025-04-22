def finddel(num):
    d = []
    for delit in range(2, round(num ** 0.5) + 1):
        if num % delit == 0:
            d.append(delit)
            d.append(num // delit)
    return set(d)


c = 0
for num in range(700_001, 1000_000):
    d = finddel(num)
    M = min(d) + max(d) if len(d) > 0 else 0
    if M % 10 == 4 and c != 5:
        print(num, M)
        c += 1