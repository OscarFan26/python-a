import turtle as t

# t.color('red')
# t.speed(0)
# t.circle(361, 361)
# for j in range(1000):
#     for i in range(4):
#         t.circle(j*10)
#         t.left(360/4)
t.pensize(10)
t.bgcolor('black')
colorlist = ['red', 'blue', 'yellow', 'brown']
for i in range(6):
	for j in range(4):
		t.color(colorlist[j])
		t.fd(100)
		t.left(90)
	t.penup()
	t.left(360 / 6)
	t.pendown()
