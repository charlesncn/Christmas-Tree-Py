import turtle

import time as tm

from turtle import *

from random import *

#background

s = Screen()

s.title(' + @ ')

w, h = 700, 700

s.setup(w, h)

s.bgcolor('white')

star = Turtle()

star.shape('circle')

star.shapesize(0.2,0.2)

star.color('red')

star.pu()

star.speed('fastest')

for i in range(650):

    x = randint(-w, w)

    y = randint(-h, h)

    star.goto(x, y)

    star.stamp()

    turtle.color('red')

    style = ('Courier', 10, 'italic')

    turtle.write("SEASON'S GREETINGS\n Merry Christmass\n\n\n\n\n\n\n\n\n\n\n\n", font=style, align='center')

    turtle.write('',align='center')

#    turtle.hideturtle()

n = 200

#turtle.goto(0, -20)

#star

turtle.pensize(6)

turtle.speed('fastest')

turtle.left(90)

turtle.forward(3*n)

turtle.color('#ffae42')

turtle.begin_fill()

turtle.left(126)

turtle.pendown()

for _ in range(5):

    turtle.forward(n/5)

    turtle.right(144)

    turtle.forward(n/5)

    turtle.left(72)

turtle.end_fill()

turtle.right(126)

#tree

turtle.pencolor('#01281a')

turtle.back(n*4.8)

def tree(d,s):

    if d <= 0:

        return

    turtle.forward(s)

    tree(d-1, s*.8)

    turtle.right(120)

    tree(d-3, s*.5)

    turtle.right(120)

    tree(d-3, s*.5)

    turtle.right(120)

    turtle.back(s)

 

turtle.pendown()

turtle.pencolor('#01281a')

tree(15, n)

turtle.back(n/2)

#bucket

turtle.color('red')

turtle.begin_fill()

turtle.left(90)

turtle.forward(-100)

turtle.left(60)

turtle.forward(100)

turtle.right(60)

turtle.forward(100)

turtle.left(300)

turtle.forward(100)

turtle.left(60)

turtle.forward(-200)

turtle.left(60)

turtle.end_fill()

#sparkles

def ornament(x, y):

    turtle.penup()

    turtle.goto(x, y)

    turtle.pencolor('#ff0000')

    turtle.pendown()

    turtle.dot(70)

    turtle.penup()

orn_pnts=[  (5, 60), (-7, 40), (10, 20), (-15, 0), (25, -20),

            (-27, -30), (7, -33), (40, -60), (-9, -63),

            (-50, -88), (62, -97),  (5, 60), (-7, 40), (10, 20), (-15, 0), (25, -20),

            (-27, -30), (7, -33), (40, -60), (-9, -63),

            (-50, -88), (62, -97),  (5, 60), (-7, 40), (10, 20), (-15, 0), (25, -20),

            (-27, -30), (7, -33), (40, -60), (-9, -63),

            (-50, -88), (62, -97), (5, 60), (-7, 40), (10, 20), (-15, 0), (25, -20),

            (-27, -30), (7, -33), (40, -60), (-9, -63),

            (-50, -88), (62, -97),  (5, 60), (-7, 40), (10, 20), (-15, 0), (25, -20),

            (-27, -30), (7, -33), (40, -60), (-9, -63),

            (-50, -88), (62, -97),  (5, 60), (-7, 40), (10, 20), (-15, 0), (25, -20),

            (-27, -30), (7, -33), (40, -60), (-9, -63),

            (-50, -88), (62, -97) , (5, 60), (-7, 40), (10, 20), (-15, 0), (25, -20),

            (-27, -30), (7, -33), (40, -60), (-9, -63),

            (-50, -88), (62, -97),  (5, 60), (-7, 40), (10, 20), (-15, 0), (25, -20),

            (-27, -30), (7, -33), (40, -60), (-9, -63),

            (-50, -88), (62, -97),  (5, 60), (-7, 40), (10, 20), (-15, 0), (25, -20),

            (-27, -30), (7, -33), (40, -60), (-9, -63),

            (-50, -88), (62, -97)  ]

for j in range(len(orn_pnts)):

    ornament(orn_pnts[j][0], orn_pnts[j][1])

    turtle.speed('slow')

turtle.penup()

turtle.goto(0, -120)

tm.sleep(20)

while True:

	pass
