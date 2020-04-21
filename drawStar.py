import turtle

def drawStar(turt, length):
    for i in range(5):
        turt.forward(length)
        turt.right(144)
james = turtle.Turtle()
window = turtle.Screen()
window.bgcolor("lightgreen")
james.color("red")
james.pensize(3)
#window.setworldcoordinates(0,0,200,200)
for i in range(5):
    drawStar(james, 20)
    james.penup()
    james.forward(40)
    james.left(144)
    james.forward(40)
    james.pendown()

window.exitonclick()
    