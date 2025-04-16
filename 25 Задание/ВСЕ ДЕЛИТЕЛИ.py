from math import ceil

def finddel(num):
    d = []
    for delit in range(1, round(num ** 0.5) + 1):
        if num % delit == 0:
            d.append(delit)
            d.append(num // delit)
    return set(d)


for num in range(1000, 10000):
    d = finddel(num)

    S = sum(d)

    if S % 100 == 23:
        print(num, S)