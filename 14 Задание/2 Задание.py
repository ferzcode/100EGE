from string import *

for x in '0123456789' + ascii_uppercase[:12]:
    number = int(f'A23{x}AC0', 22) + int(f'GB{x}21670', 22)
    if number % 21 == 0:
        print(number // 22)