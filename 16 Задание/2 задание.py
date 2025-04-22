def f(x, y):
    if x == y: return 1
    elif x > y or x == 35: return 0
    else: return f(x + 1, y) + f(x + 2, y) + f(x * 2, y)

print(f(7, 13) * f(13, 15) * f(15, 51))

# Если траектория содержит число - учитываем в printe
# Если траектория НЕ содержит число - учитываем в условии на 0