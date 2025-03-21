f = open('26var01.txt')

kletki, horizont, vertex = [int(x) for x in f.readline().split()]
field = [horizont + 1] * (vertex + 1)
# print(field)

for i in range(kletki):
    gor, vert = [int(x) for x in f.readline().split()]

    field[vert] = min(field[vert])