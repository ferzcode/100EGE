from re import *

f = open('24_21421.txt').readline()

reg = r'([1-9AB][0-9AB]*[02468A])'

maxi = max(len(s.group()) for s in (finditer(reg, f)))
print(maxi)


# l = []
# for sovp in findall(reg, f):
#     l.append(len(sovp))
#
# print(max(l))

