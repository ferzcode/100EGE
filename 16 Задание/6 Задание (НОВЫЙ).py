a = [0] * 2025

a[1] = 1

for i in range(2, 2025):
    a[i] = i * a[i - 1]

print((a[2024]//4 + a[2023]) // a[2022])