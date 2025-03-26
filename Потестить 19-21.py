from turtle import *

tracer(0)
screensize(10000, 10000)

k = 15
for i in range(3):
    forward(7 * k)
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
for x in range(-50 * k, 50 * k, k):
    for y in range(-50 * k, 50 * k, k):
        goto(x, y)
        dot(3, "red")

update()
done()
