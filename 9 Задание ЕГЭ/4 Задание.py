#Откройте файл электронной таблицы, содержащей в каждой строке шесть натуральных чисел. Определите количество строк
# таблицы, содержащих числа, для которых выполнены оба условия:
#– в строке только одно число повторяется трижды, остальные числа различны;
#– квадрат суммы всех повторяющихся чисел строки больше квадрата суммы всех её неповторяющихся чисел.
# ответе запишите только число.

count = 0
for s in open('4 Задание.txt'):

    stroka = [int(number) for number in s.split()]

    povtorki = [number for number in stroka if stroka.count(number) == 3]
    np = [number for number in stroka if stroka.count(number) == 1]

    if len(povtorki) == 3 and len(np) == 3: # len(np) обязательно для проверки!! Числа должны быть различными
        if (sum(povtorki) ** 2) > (sum(np) ** 2):
            count += 1

print(count)



















