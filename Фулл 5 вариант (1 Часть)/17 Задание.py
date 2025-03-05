f = open('17 Задание.txt')
ar = [int(x) for x in f]

minik = 100000
for i in range(len(ar)):
    if ar[i] % 100 == 25:
        minik = min(minik, ar[i])

count = 0
max_summ = 0
for i in range(len(ar) - 2):
    troyka = [ar[i], ar[i + 1], ar[i + 2]]
    odno = [x for x in troyka if 10 <= x <= 99] # 1 ЧИСЛО

    if len(odno) == 1 and sum(troyka) < minik:
        count += 1
        max_summ = max(sum(troyka), max_summ)
print(count, max_summ)
