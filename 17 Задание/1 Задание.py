def proverka(num):
    return 9999 < abs(num) < 100_000 and abs(num) % 100 == 43


m = [int(x) for x in open('17_19249.txt')]
max_element = 0

for elem in m:
    if proverka(elem) == True:
        max_element = max(elem, max_element)

minik = 1000000000000000
count = 0
for i in range(len(m) - 2):
    if (proverka(m[i]) or proverka(m[i + 1]) or proverka(m[i + 2])) and \
            (m[i] ** 2 + m[i + 1] ** 2 + m[i + 2] ** 2) <= max_element ** 2:
        count += 1
        minik = min(minik, m[i] ** 2 + m[i + 1] ** 2 + m[i + 2] ** 2)

print(count, minik)