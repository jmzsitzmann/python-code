import random, turtle

def moveTurt(window, t1):
    xbound = window.window_width() / 2
    ybound = window.window_height() / 2
    xcoord = t1.xcor()
    ycoord = t1.ycor()
    coin = random.randrange(0,2)
    t1.shape("turtle")
    t1.goto(random.randrange(-xbound,xbound),random.randrange(-ybound, ybound))
    if coin==0:
        t1.penup()
        t1.forward(50)
        t1.left(60)
    if coin==1:
        t1.penup()
        t1.forward(50)
        t1.right(60)
jojo = turtle.Turtle()
jp = turtle.Turtle()
wn = turtle.Screen()

def IsInScreen(window2, t2):
    xbound = window2.window_width() / 2
    ybound = window2.window_height() / 2
    xcoord = t2.xcor()
    ycoord = t2.ycor()
    if(xcoord < xbound and xcoord > -xbound):
        if(ycoord < ybound and ycoord > -ybound):
            return True
        else:
            return False
    else:
        return False
while IsInScreen(wn, jojo) and IsInScreen(wn, jp):
    moveTurt(wn, jojo)
    moveTurt(wn, jp)
        
