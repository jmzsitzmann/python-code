import turtle
wn = turtle.Screen()
def drawPolygon(turt, x, sides):
    for i in range(sides):
        turt.forward(x)
        turt.left(360/sides)
def drawCircle(anyturt, radius):
    circumference = 2*3.14*radius
    x = circumference / 360
    drawPolygon(tess, x, 360)
    tess.left(90)
    tess.penup()
    tess.forward(radius)
tess = turtle.Turtle()
drawCircle(tess, 100)
wn.exitonclick()