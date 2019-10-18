import turtle
import math

def drawLine(p1, p2):
    # turtle.setheading(0)

    # Compute the distance between p1 and p2
    d = math.sqrt((p2[0] - p1[0]) * (p2[0] - p1[0]) + (p2[1] - p1[1]) * (p2[1] - p1[1]))

    if p1[0] <= p2[0]: # p2 is on the right of p1
        angle = math.asin((p2[1] - p1[1]) / d)
    else:
        angle = -math.asin((p2[1] - p1[1]) / d) + math.pi

    turtle.penup()
    turtle.goto(p1[0], p1[1])
    turtle.pendown()
    turtle.radians()
    turtle.setheading(angle)
    turtle.forward(d)
