import turtle
jp = turtle.Turtle()
def drawColoredAsterik(turt, length):
    for i in range(6):
        turt.color("blue")
        turt.forward(length/2)
        turt.backward(length)
        turt.forward(length/2)
        turt.left(30)
length = int(input("what width asterik would you like?"))
wn = turtle.Screen()

for i in range(20):
    drawColoredAsterik(jp, length)
    jp.forward(40)
    jp.right(10)    

wn.exitonclick()    

