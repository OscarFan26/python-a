import turtle as t

t.speed(0)
for x in range(3):
	t.penup()
	t.goto(-200, 175 - (x - 1) * 100)
	t.pendown()
	for j in range(3):
		for i in range(4):
			t.fd(100)
			t.right(90)
		t.forward(100)


def X():
	t.pendown()
	t.seth(45)
	t.fd(40)
	t.left(180)
	t.fd(80)
	t.left(180)
	t.fd(40)
	t.right(90)
	t.fd(40)
	t.left(180)
	t.fd(80)
	t.penup()
	t.goto(0, 0)


input_position = t.textinput('position_enter', '请输入您要走的位置:')

positon_0x, positon_0y = -200 + 50, 175 + 50
positon_1x, positon_1y = -200 + 50 * 3, 175 + 50
positon_2x, positon_2y = -200 + 50 * 5, 175 + 50
positon_3x, positon_3y = -200 + 50, 175 - 50
positon_4x, position_4y = -200 + 50 * 3, 175 - 50
positon_5x, positon_5y = -200 + 50 * 5, 175 - 50
positon_6x, positon_6y = -200 + 50, 175 - 50 * 3
positon_7x, positon_7y = -200 + 50 * 3, 175 - 50 * 3
positon_8x, positon_8y = -200 + 50 * 5, 175 - 50 * 93

if input_position == '0':
	t.penup()
	t.goto(positon_0x, positon_0y)
	t.pendown()
	X()
if input_position == '1':
	t.penup()
	t.goto(positon_1x, positon_1y)
	t.pendown()
	X()
if input_position == '2':
	t.penup()
	t.goto(positon_2x, positon_2y)
	t.pendown()
	X()
if input_position == '3':
	t.penup()
	t.goto(positon_3x, positon_3y)
	t.pendown()
	X()
if input_position == '4':
	t.penup()
	t.goto(positon_4x, position_4y)
	t.pendown()
	X()
if input_position == '5':
	t.penup()
	t.goto(positon_5x, positon_5y)
	t.pendown()
	X()
if input_position == '6':
	t.penup()
	t.goto(positon_6x, positon_6y)
	t.pendown()
	X()
if input_position == '7':
	t.penup()
	t.goto(positon_7x, positon_7y)
	t.pendown()
	X()
if input_position == '8':
	t.penup()
	t.goto(positon_8x, positon_8y)
	t.pendown()
	X()

t.done()
