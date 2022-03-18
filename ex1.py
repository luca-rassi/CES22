import turtle


def draw_squares(t, sz, n):
    # draws n centered squares, the inner one with side sized sz
    for i in range(n):
        for j in range(4):
            t.fd(sz + i*sz)
            t.left(90)
        set_turtle(t, sz/2)


def set_turtle(t, d):
    #set the turtle without drawning it in d unit to the left and d units down
    t.penup()
    t.bk(d)
    t.right(90)
    t.fd(d)
    t.left(90)
    t.pendown()


wn = turtle.Screen()
wn.bgcolor("lightgreen")
wn.title("Ex. 1")
alex = turtle.Turtle()
alex.pensize(3)
alex.color(0.7, 0.5, 0.7)
length = 20
rp = 5
draw_squares(alex, length, rp)


wn.mainloop()
