for x in range(1, 2031):
    num = 7 ** 170 + 7 ** 100 - x

    k = 0
    while num > 0:
        if num % 7 == 0:
            k += 1
        num //= 7

    if k == 71:
        print(x)


# ПЕРЕСДАЧА 04.07.2024 ЕГЭ

# for x in range(1, 2031):
#     num = 6 ** 260 + 6 ** 160 + 6 ** 60 - x
#
#     k = 0
#     while num > 0:
#         if num % 6 == 0:
#             k += 1
#         num //= 6
#     if k == 202:
#         print(x)