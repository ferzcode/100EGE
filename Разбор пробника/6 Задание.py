from turtle import *
tracer(0)

k = 30
for i in range(10):
    right(120)
    forward(12 * k)
    right(60)
    forward(12 * k)
update()
penup()

for x in range(-20 * k, 20 * k, k):
    for y in range(-20 * k, 20 * k, k):
        goto(x, y)
        dot(3, "red")
done()