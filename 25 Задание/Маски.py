from fnmatch import *

for x in range(0, 10 ** 11, 154682):
    if fnmatch(str(x), '*192?3*68'):
        print(x, x // 154682)

for x in range(0, 10 ** 10, 98591):
    if fnmatch(str(x), '5?2*3?3?'):
        print(x, x // 98591)

for x in range(0, 10 ** 10, 1917):
    if fnmatch(str(x), '3?12?14*5'):
        print(x, x // 1917)