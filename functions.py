import turtle
def drawMulticolorSquare(t, sz):
    for i in ["red", "purple", "hotpink", "blue"]:
        t.color(i)
        t.forward(sz)
        t.left(90)
         
wn = turtle.Screen()
wn.bgcolor("lightgreen")
alex = turtle.Turtle()
alex.pensize(3)
size = 20

for x in range(15):
    drawMulticolorSquare(alex, size)
    size = size + 10
    alex.forward(10)
    alex.right(18)
wn.exitonclick()

# alex.stamp()
# for i in range(20):
#    alex.penup()  
#    alex.forward(50)
#    alex.stamp()
#    alex.backward(50)
#    alex.right(22.5)

