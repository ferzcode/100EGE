# Откройте файл электронной таблицы, содержащей в каждой строке семь натуральных чисел.
#
# Определите наибольший номер строки таблицы, для чисел которой выполнены оба условия:
#     – в строке есть ровно два числа, каждое из которых повторяется трижды, и одно число без повторений;
#     – среднее арифметическое повторяющихся чисел строки меньше неповторяющегося числа.
# В ответе запишите только число.

poryadkoviy_nomer = 0

for s in open('3 Задание.txt'):
    poryadkoviy_nomer += 1

    stroka = [int(number) for number in s.split()]

    povtorki = [number for number in stroka if stroka.count(number) == 3]
    sigma = [number for number in stroka if stroka.count(number) == 1]

    sr_arifm = sum(povtorki) / len(povtorki) if len(povtorki) > 0 else 0 # Если длина повторок больше 0, то ср. арифметическое считаем так

    if len(povtorki) == 6 and sr_arifm < sigma[0]:
        print(poryadkoviy_nomer)
