# 绘制蟒蛇 turtle 绘图库
import turtle as t
t.setup(900, 400, 200, 200)
t.penup()
t.fd(-400)
t.pendown()
t.pensize(15)
t.pencolor("red")
t.seth(-50)
for i in range(4):
    t.circle(50, 100)
    t.circle(-50, 100)
t.circle(50, 50)
t.fd(50)
t.circle(10, 180)
t.fd(25)
t.done()




