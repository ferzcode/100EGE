from turtle import *
tracer(0)
screensize(10000, 10000)

k = 10
for i in range(3):
    forward(27 * k)
    right(90)
    forward(12 * k)
    right(90)

penup()
forward(4 * k)
right(90)
forward(6 * k)
left(90)
pendown()

for i in range(4):
    forward(83 * k)
    right(90)
    forward(77 * k)
    right(90)

penup()
for x in range(-70 * k, 50 * k, k):
    for y in range(-55 * k, 80 * k, k):
        goto(x, y)
        dot(3, "red")


update()
done()