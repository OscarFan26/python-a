import turtle as t
import math


def face():
    t.penup()
    t.goto(0, -200)
    t.pendown()
    t.circle(200)


def left_eye():
    t.penup()
    t.goto(-100, 50)
    t.pendown()
    t.pencolor("blue")
    t.begin_fill()
    t.circle(20)
    t.end_fill()


def right_eye():
    t.penup()
    t.goto(100, 50)
    t.pendown()
    t.pencolor("blue")
    t.begin_fill()
    t.circle(20)
    t.end_fill()


def nose():
    t.penup()
    t.goto(0, 50)
    t.right(60)
    t.color("black")
    t.pendown()
    for i in range(3):
        t.fd(50*math.sqrt(3))
        t.right(120)


def mouth():
    t.penup()
    t.goto(-150, -70)
    t.pendown()
    t.goto(0, -170)
    t.goto(150, -70)


t.speed(0)

face()
left_eye()
right_eye()
nose()
mouth()

t.hideturtle()
t.done()
