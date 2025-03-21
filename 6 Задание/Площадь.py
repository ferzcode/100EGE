from turtle import *
tracer(0)
screensize(10000, 10000)

k = 10
forward(25 * k)
right(45)
forward(50 * k)
penup()
backward(50 * k)
right(45)
forward(15 * k)
left(90)
forward(30 * k)
pendown()
right(180)
forward(60 * k)
backward(5 * k)
right(90)
forward(31 * k)

penup()
for x in range(-70 * k, 50 * k, k):
    for y in range(-55 * k, 80 * k, k):
        goto(x, y)
        dot(3, "red")


update()
done()