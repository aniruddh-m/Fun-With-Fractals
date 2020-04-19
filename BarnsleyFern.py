import turtle
import random

def setupPen(t):
    t.speed(0)
    t.penup()
    t.pendown()
    t.hideturtle()

if __name__ == "__main__":    
    window = turtle.Screen()
    window.setup(0.75, 0.75)
    t = turtle.Turtle()

    setupPen(t)

    maxNumPoints = 1000

    x = 0
    y = 0

    for _ in range(maxNumPoints):
        randomNumber = random.randint(1, 100)
    
        if(randomNumber == 1):
            xtemp = 0
            ytemp = 0.16*y
        elif(randomNumber <= 86):
            xtemp = (0.85*x) + (0.04*y)
            ytemp = (0.85*y) + 1.6 - (0.04*x)
        elif(randomNumber <= 93):
            xtemp = (0.20*x) - (0.26*y)
            ytemp = (0.23*x) + (0.22*y) + 1.6
        else:
            xtemp = (0.28*y) - (0.15*x)
            ytemp = (0.26*x) + (0.24*y) + 0.44

        x = xtemp
        y = ytemp

        t.penup()
        t.setpos(30*x-250, 30*y-250)
        t.dot()
        t.pendown()


    turtle.done()