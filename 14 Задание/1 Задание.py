from string import *

for x in '0123456789' + ascii_uppercase[:8]:
    number = int(f'11H{x}05', 18) + int(f'3F{x}54{x}8', 18) + int(f'G{x}{x}{x}9', 18)
    if number % 14 == 0:
        print(number // 14)