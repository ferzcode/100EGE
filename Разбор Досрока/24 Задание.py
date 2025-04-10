from re import *

s = open('24_21421.txt').readline()
sub = '[1-9AB][0-9AB]*[02468A]'

maxl = 0
for stroka in findall(sub, s):
    maxl = max(maxl, len(stroka))

print(maxl)