from re import *

f = open('24_19751.txt').readline()

num = r'[1-9]+'
reg = rf'[A]{num}(\+{num})'

for c in findall(reg, f):
    print(c)