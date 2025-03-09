maxi = 0
for x in range(70000, 9, -1):
    num = 5 ** 2025 + 5 ** 400 - x

    k = 0
    while num > 0:
        if num % 5 == 4:
            k += 1
        num //= 5

    if k == 399:
        print(x)
        break
#     maxi = max(maxi, k)
# print(maxi)