from itertools import *

s = '234 157 147 138 268 58 23 456'.split() # Переписываем все связи из таблицы
v = 'BC BE BD CH EH HF DE DG FG FA GA'.split() # Записываем все дороги с графа

print(*range(1, 9)) # Печатаем номера пунктов сверху
for p in permutations('ABCDEFGH'):
    if all(str(p.index(b) + 1) in s[p.index(a)] for a, b in v):
        print(*p)

# Вывод суммы из A -> G + D -> E
# 6 -> 8 + 4 -> 1
print(4 + 7)