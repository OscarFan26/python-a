# # # -*- encoding = utf-8 -*- #
import turtle as t

# # for i in range(4):
# #     t.fd(100)
# #     t.left(90)
# t.penup()
# t.goto(-100,-30)
# t.pendown()
t.pencolor('black')
t.pensize(1)
t.title('turtle one')
# # for j in range(100):
# #     t.speed(10)
# #     t.fd(j*5)
# #     t.left(360/3)
# #
# # t.done()
colorlist = ['red', 'blue', 'yellow', 'brown', 'purple', 'orange', 'green',
             'light green', 'dark blue', 'dark blue', 'grey5']

t.penup()
t.speed(10)
t.goto(0, 0)
t.pendown()
for vs in range(11):
	for i in range(4):
		t.pencolor(colorlist[vs])
		t.fd((vs + 1) * 12)
		t.left(360 / 4)
	t.penup()
	t.goto(-(vs + 1) * 4, -(vs + 1) * 4)
	t.pendown()
t.done()
