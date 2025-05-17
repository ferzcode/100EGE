print(int('AB', 16))
print(int('500', 8))
print(int('111110', 2))

m = []
while True:
    a = int(input())
    if a != 0:
        m.append(a)
    else:
        break
    
count = 0
summa = 0
for i in range(len(m)):
    if 10 <= m[i] <= 99:
        summa += m[i]
        count += 1

if count == 0:
    print("NO")
else:
    print(round(summa / count))

    
