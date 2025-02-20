# Откройте файл электронной таблицы, содержащей в каждой строке пять натуральных чисел.
# Определите количество строк таблицы, в которых сумма наибольшего и наименьшего чисел не меньше суммы трех оставшихся.
#
# В ответе запишите только число.

count = 0
for s in open('1 Задание.txt'):
    stroka = [int(number) for number in s.split()]

    tri_ostavshihsya = sum(stroka) - max(stroka) - min(stroka)
    summa_min_max = max(stroka) + min(stroka)

    if summa_min_max >= tri_ostavshihsya:
        count += 1

print(count)