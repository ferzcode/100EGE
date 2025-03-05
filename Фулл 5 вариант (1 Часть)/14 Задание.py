import string
from string import *

alp = string.digits + string.ascii_uppercase[:13]

for x in alp:
    numb = int(f'1{x}1{x}1{x}1{x}1', 23) + int(f'20{x}24', 23) + int(f'1{x}235', 23)
    if numb % 22 == 0:
        print(numb // 22)