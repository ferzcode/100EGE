from turtle import *

screensize(10000, 10000)
tracer(0)
k = 10
for i in range(3):
    fd(27 * k)
    rt(90)
    fd(12 * k)
    rt(90)
up()
fd(4 * k)
rt(90)
fd(6 * k)
lt(90)
pd()

for i in range(4):
    fd(83 * k)
    rt(90)
    fd(77 * k)
    rt(90)

up()
for x in range(-100 * k, 100 * k, k):
    for y in range(-100 * k, 100 * k, k):
        goto(x, y)
        dot(3, "red")

update()
done()