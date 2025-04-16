from re import *
f = open('24_19969.txt').readline()

reg = r'[a-z]+@[a-z]+\.+[a-z]+'
print(max(len(s.group()) for s in finditer(reg, f)))