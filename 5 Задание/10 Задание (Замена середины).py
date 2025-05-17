a = []
for N in range(4, 1000):
    b = bin(N)[2:]
    if N % 2 == 0:
        b = b + b[-2] + b[-1]
    else:
        b = b + b[-3] + b[-2] + b[-1]
    R = int(b, 2)
    if R > 256:
        a.append(N)
print(min(a))