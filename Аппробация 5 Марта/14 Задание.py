# maxi = 0
for x in range(1, 2031):
    number = 7 ** 170 + 7 ** 100 - x

    new = ''
    while number > 0:
        new += str(number % 7)
        number //= 7
    new = new[::-1]

    if new.count('0') == 73:
        print(x)
    # maxi = max(maxi, new.count('0'))
# print(maxi)