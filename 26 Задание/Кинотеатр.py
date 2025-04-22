f = open('26_17537.txt')
N, M, K = map(int, f.readline().split())

min_ryad = [M + 1] * (K + 2)

for i in range(N):
    ryad, mesto = map(int, f.readline().split())
    if ryad < min_ryad[mesto]:
        min_ryad[mesto] = ryad

max_r = 0  # Максимальный найденный ряд
best_k = 0  # Номер места в лучшей паре

for k in range(1, K):
    r = min(min_ryad[k], min_ryad[k + 1]) - 1
    if r > max_r:
        max_r = r
        best_k = k
    elif r == max_r and k > best_k:
        best_k = k

    # if r == 9991:
    #     print(k, k + 1)

print(max_r, best_k)

