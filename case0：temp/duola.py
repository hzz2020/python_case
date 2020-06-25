import turtle as t

t.setup(1000, 800, 100, 100)

# t.color('#111111', '#198EDB')

t.fillcolor('#198EDB')

t.pencolor('#FFFFFF')
t.circle(80, 45)
t.begin_fill()
t.pencolor('#222222')
t.circle(80, 270)
t.end_fill()
t.pencolor('#FFFFFF')
t.circle(80, 45)

t.fillcolor('#FFFFFF')
t.pencolor('#FFFFFF')
t.circle(60, 45)
t.begin_fill()
t.pencolor('#222222')
t.circle(60, 270)
t.end_fill()
t.pencolor('#FFFFFF')
t.circle(60, 45)


t.penup()
t.right(90)
t.fd(150)
t.pendown()
t.left(90)

t.fillcolor("red")
t.begin_fill()
# 绘制五角星外边
for i in range(5):
    t.forward(220)
    t.right(144)
t.fd(84)
# 绘制五角星内边
for i in range(5):
    t.fd(52)
    t.right(72)
t.end_fill()
t.done()

