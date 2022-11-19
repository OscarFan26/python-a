import turtle as t

t.speed(-100)
t.penup()
t.goto(-280, 280)
t.pendown()

for y in range(1, 9):
	if y % 2 == 0:
		t.goto(-280, 280 - (y - 1) * 50)
		t.pendown()
		for x in range(8):
			if x % 2 == 0:
				t.fillcolor('brown')
			else:
				t.fillcolor('white')
			t.begin_fill()
			for i in range(4):
				t.forward(50)
				t.right(90)
			t.end_fill()
			t.forward(50)
		t.penup()
	else:
		t.goto(-280, 280 - (y - 1) * 50)
		t.pendown()
		for x in range(8):
			if x % 2 == 0:
				t.fillcolor('white')
			else:
				t.fillcolor('brown')
			t.begin_fill()
			for i in range(4):
				t.forward(50)
				t.right(90)
			t.end_fill()
			t.forward(50)
		t.penup()
t.hideturtle()
t.done()
