a = [int(x) for x in open('17_21903.txt')]

podh = [num for num in a if abs(num) % 100 == 15 and 100 <= abs(num) <= 999]
mini = min(podh)

# res = []
c = 0
minimum = 1000000000000000000000000000

for i in range(len(a) - 2):
    b = [a[i], a[i + 1], a[i + 2]]
    if (b[0] > 0 and b[1] > 0 and b[2] > 0) or (b[0] < 0 and b[1] < 0 and b[2] < 0):
        if max(b) * min(b) > mini ** 2:
            c += 1
            minimum = min(minimum, max(b) * min(b))
            # res.append([min(b) * max(b)])

# print(len(res), min(res))