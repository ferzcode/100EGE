num = 3 ** 2020 - 3 ** 1020 + 9 ** 800 - 81
count = 0
while num > 0:
    if num % 3 == 2:
        count += 1
    num //= 3
print(count)