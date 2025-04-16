def finddel(num):
    d = []
    for delit in range(2, round(num ** 0.5) + 1):
        if num % delit == 0:
            d.append(delit)
            d.append(num // delit)
    return set(d)

# def p(num):
#     return num > 1 and all(num % d != 0 for d in range(2, round(num ** 0.5) + 1))

c = 0
for num in range(9_500_001, 10_000_000):
    d = finddel(num)

    prostie = [dp for dp in d if len(finddel(dp)) == 0]
    F = int(sum(prostie) / len(prostie)) if len(prostie) > 0 else 0

    if F != 0 and F % 813 == 0 and c != 5:
        print(num, F)
        c += 1