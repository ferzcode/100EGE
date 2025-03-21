from turtle import *
tracer(0)
screensize(10000, 10000)

k = 10

for i in range(9):
    forward(30 * k)
    right(90)
    forward(12 * k)
    right(90)

penup()
left(270)
forward(5 * k)
left(90)
pendown()

for i in range(2):
    forward(24 * k)
    right(90)
    forward(28 * k)
    right(90)

penup()
for x in range(-70 * k, 50 * k, k):
    for y in range(-55 * k, 80 * k, k):
        goto(x, y)
        dot(3, "red")


update()
done()