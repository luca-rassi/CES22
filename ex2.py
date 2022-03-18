from operator import length_hint
import turtle


def draw_poly(t, n, sz):
    # draws a regular polygon of n sides of size sz
    for i in range(n):
        t.fd(sz)
        t.left(360/n)


wn = turtle.Screen()
wn.bgcolor("lightgreen")
wn.title("Ex. 2")
tess = turtle.Turtle()
tess.pensize(3)
tess.color((0.8, 0.5, 0.8))
draw_poly(tess, 8, 50)

wn.mainloop()
