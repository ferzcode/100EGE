from turtle import *

tracer(0)

k = 20
for i in range(2):
    fd(17 * k)
    lt(90)
    fd(10 * k)
    lt(90)

penup()
bk(4 * k)
rt(90)
bk(3 * k)
lt(90)
pendown()

for i in range(2):
    fd(40 * k)
    rt(90)
    fd(10 * k)
    rt(90)

penup()
for x in range(-9 * k, 39 * k, k):
    for y in range(-10 * k, 11 * k, k):
        goto(x, y)
        dot(3, "red")
update()
done()