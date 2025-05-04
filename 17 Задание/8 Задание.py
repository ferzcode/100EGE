a = [int(x) for x in open('17_21712.txt')]


def podhod(num1, num2, num3):
    return (abs(num1) % 10 == 6 and 1000 <= abs(num1) <= 9999) + (abs(num2) % 10 == 6 and 1000 <= abs(num2) <= 9999) + (
                abs(num3) % 10 == 6 and 1000 <= abs(num3) <= 9999)


chetirki = [num for num in a if num > 0 and 1000 <= num <= 9999 and num % 10 == 6]
minik = min(chetirki)
res = []

for i in range(len(a) - 2):
    if podhod(a[i], a[i + 1], a[i + 2]) == 1 and (a[i] + a[i + 1] + a[i + 2]) <= minik:
        res.append(a[i] + a[i + 1] + a[i + 2])

print(len(res), max(res))
