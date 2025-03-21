from turtle import *
tracer(0)
screensize(10000, 10000)

k = 15
for i in range(9):
    forward(27 * k)
    right(90)
    forward(30 * k)
    right(90)

penup()
forward(3 * k)
right(90)
forward(6 * k)
left(90)
pendown()

for i in range(9):
    forward(77 * k)
    right(90)
    forward(66 * k)
    right(90)

penup()
for x in range(-52 * k, 50 * k, k):
    for y in range(-55 * k, 50 * k, k):
        goto(x, y)
        dot(3, "red")


update()
done()