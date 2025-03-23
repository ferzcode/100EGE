from turtle import *

screensize(10000, 10000)
k = 15

tracer(0)
for i in range(4):
    forward(27 * k)
    right(90)
    forward(21 * k)
    right(90)

penup()
forward(3 * k)
right(90)
forward(7 * k)
left(90)
pendown()

for i in range(4):
    forward(73 * k)
    right(90)
    forward(91 * k)
    right(90)

penup()
for x in range(-20 * k, 60 * k, k):
    for y in range(-50 *k, 60 * k, k):
        goto(x, y)
        dot(3, "red")

update()
done()