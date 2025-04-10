# from turtle import *
# tracer(0)
#
# k = 15
#
# right(30)
# for i in range(3):
#     right(150)
#     forward(6 * k)
#     right(30)
#     forward(12 * k)
#
# penup()
#
# for x in range(-50 * k, 50 * k, k):
#     for y in range(-50 * k, 50 * k, k):
#         goto(x, y)
#         dot(3, "red")
#
#
#
# update()
# done()


from turtle import *
k = 1000
screensize(10000,10000)
speed(0)
left(90)
begin_fill()
rt(30)
for i in range(2):
    rt(150)
    fd(6 * k)
    rt(30)
    fd(12 * k)
end_fill()

c = getcanvas()
cnt = 0
for x in range(-200,200):
    for y in range(-200,200):
        if c.find_overlapping(x * k,y * k,x * k,y * k) == (5,):
            cnt += 1
print(cnt)

done()