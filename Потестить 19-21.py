# #17
# def f(n, m):
#     return (abs(n) % 10 == 7) + (abs(m) % 10 == 7)
#
# m = [int(x) for x in open('C:/Users/and18/Downloads/Telegram Desktop/Файлы к пробнику Март/17 Задание.txt')]
# res = []
# for i in range(len(m) - 1):
#     if f(m[i], m[i + 1]) == 2:
#         res.append(abs(m[i] - m[i + 1]))
# print(len(res), min(res))

print('x y z w')
for x in range(2):
    for y in range(2):
        for z in range(2):
            for w in range(2):
                F = (not(x <= y)) or ((not(w)) <= (not(z))) or w
                if F == 0:
                    print(x, y, z, w)