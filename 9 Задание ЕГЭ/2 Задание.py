# Откройте файл электронной таблицы, содержащей в каждой строке четыре натуральных числа.
# Определите сумму номеров всех строк таблицы, содержащих числа, для которых выполнены оба условия:
# – в строке нет повторяющихся чисел;
# – квадрат суммы наибольшего и наименьшего чисел больше суммы кубов оставшихся чисел.
# В ответе запишите только число.

count = 0
poryadkoviy_nomer = 0

itog = 0
for s in open('2 Задание.txt'):

    poryadkoviy_nomer += 1

    stroka = [int(number) for number in s.split()]

    stroka.sort()
    kvadrat_summa = (max(stroka) + min(stroka)) ** 2
    summa_kubov = stroka[1] ** 3 + stroka[2] ** 3

    if len(stroka) == len(set(stroka)) and kvadrat_summa > summa_kubov:
        itog += poryadkoviy_nomer

print(itog)