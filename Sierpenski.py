import turtle

def Sierpenski(t, left, top, right, side, numIter):
    t.penup()
    t.setpos(left)
    t.pendown()

    # Draw triangle
    t.setheading(60)
    t.forward(side)
    t.setheading(300)
    t.forward(side)
    t.setheading(180)
    t.forward(side)

    if(numIter == 0):
        return

    else:
        numIter = numIter - 1
        side = side/2  
        Sierpenski(t, left, (side/2, side*(3**(1/2)/2)), (side, 0), side, numIter)
        Sierpenski(t, (side/2+left[0], side*(3**(1/2)/2)+left[1]), top, (3*side/2+left[0], side*(3**(1/2)/2)+left[1]), side, numIter)
        Sierpenski(t, (side+left[0], left[1]), (side+left[0], side*(3**(1/2)/2)), (left[0]+right[0], right[1]), side, numIter)

window = turtle.Screen()
t = turtle.Turtle()

side = 150
numIter = 3

turtle.setworldcoordinates(-1, -1, side, side)

t.hideturtle()
Sierpenski(t, (0, 0), (side/2, side*(3**(1/2)/2)), (side, 0), side, numIter)

turtle.done()