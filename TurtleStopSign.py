#CS175L
#ChristopherDeTullio
#TurtleGraphicsSTOPSign

import math
import turtle

#Constants
WINDOW_WIDTH = 400
WINDOW_HEIGHT = 400
ANIMATION_SPEED = 0
NUM_SIDES = 8
LENGTH = 100
ANGLE = 45
TEXT_X = -5
TEXT_Y = -10

screen = turtle.Screen()
screen.bgcolor('white')
turtle.setup(WINDOW_WIDTH,WINDOW_HEIGHT)

t = turtle.Turtle()

def draw_stopsign(t,x,y, length):
    t.penup()
    t.setpos(x - LENGTH/2, y + LENGTH/2 / (math.pi/8))
    t.pendown()
    t.color('white','red')
    t.pensize(LENGTH // 10)
    t.begin_fill()

    for i in range(8):
        t.forward(LENGTH)
        t.right(45)
    t.end_fill()

    fontsize = int(LENGTH / 2)
    t. penup()
    t.setpos(x, y - fontsize / 2)
    t. pendown()
    t.write('STOP', move=False, align='center', font=('Arial', '45'))
    t.hideturtle()
draw_stopsign(t, 0, 0, 100)

def draw_redborder(x,y, LENGTH):
    w = turtle.Turtle()
    w.penup()
    w.setpos(-60,150)
    w.pendown()
    w.color('red')
    w.pensize(LENGTH // 6)
    w.hideturtle()
    for j in range(8):
        w.forward(117)
        w.right(45)
        
draw_redborder(0,0,100)   
turtle.mainloop()
turtle.draw_redborder()
