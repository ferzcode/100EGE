maxi = 0
for x in range(1, 2031):
    num = 7 ** 170 + 7 ** 100 - x

    count_0 = 0
    while num > 0:
        if num % 7 == 0:
            count_0 += 1
        num //= 7

    # print(x, count_0)
    if count_0 == 73:
        print(x)
    # maxi = max(count_0, maxi)
# print(maxi)a