import turtle

def drawSpiral(turt, angle):
    x = 1
    for i in range(50):
        turt.forward(x)
        turt.left(angle)
        x = x+2
dad = turtle.Turtle()
window = turtle.Screen()
window = window.bgcolor("lightblue")
dad.color("red")
dad.penup()
dad.backward(200)
dad.pendown()
drawSpiral(dad, 90)
dad.penup()
dad.home()
dad.forward(100)
dad.pendown()
drawSpiral(dad, 89)

window.exitonclick()
