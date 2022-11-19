import turtle as t

def draw_tree(branch_length):
    if branch_length > 5:
        t.fd(branch_length)
        t.right(20)
        draw_tree(branch_length - 20)
        t.left(40)
        draw_tree(branch_length - 20)
        t.right(20)
        t.backward(branch_length)

t.left(90)
t.up()
t.backward(200)
t.down()
t.color("green")
draw_tree(100)
t.done()