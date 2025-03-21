from turtle import *
tracer(0)
screensize(10000, 10000)

k = 15
for i in range(7):
    forward(5 * k)
    left(72)

penup()
for x in range(-52 * k, 50 * k, k):
    for y in range(-55 * k, 50 * k, k):
        goto(x, y)
        dot(3, "red")


update()
done()