from turtle import *

tracer(0)
screensize(10000, 10000)

k = 30
for i in range(3):
    pendown()
    for j in range(2):
        forward(10 * k)
        right(90)
        forward(10 * k)
        right(90)
    penup()
    forward(5 * k)
    right(90)
    forward(5 * k)
    left(90)

penup()
for x in range(-20 * k, 20 * k, k):
    for y in range(-20 * k, 20 * k, k):
        goto(x, y)
        dot(3, "red")

update()
done()