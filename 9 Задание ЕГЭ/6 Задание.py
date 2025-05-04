nomer = 0
res = []

for stroka in open('6 Задание.txt'):
    s = [int(x) for x in stroka.split()]
    nomer += 1

    maxi = max(s)
    mini = min(s)
    sr_ostatki = (sum(s) - maxi - mini) / 5

    if s[0] > s[1] > s[2] > s[3] > s[4] > s[5] > s[6] and (maxi + mini) / 2 > sr_ostatki:
       res.append([nomer, sum(s)])

print(min(res)[1])

# copy = reversed(sorted(s))
# if copy == s:
