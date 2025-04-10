from string import *

for x in digits + ascii_uppercase[:11]:
    s = int(f'82934{x}2', 21) + int(f'2924{x}{x}7', 21) + int(f'67564{x}8', 21)
    if s % 20 == 0:
        print(s // 20)
        break