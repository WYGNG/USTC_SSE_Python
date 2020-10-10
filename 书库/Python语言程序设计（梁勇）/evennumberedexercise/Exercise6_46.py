import turtle
import math
from UsefulTurtleFunctions import drawLine

def drawPolygon(x = 0, y = 0, radius = 50, numberOfSides = 3):
    angle = 2 * math.pi / numberOfSides

    # Connect points for the polygon
    for i in range(numberOfSides + 1):  
        for j in range(numberOfSides + 1):  
             drawLine(x + radius * math.cos(i * angle),
                y - radius * math.sin(i * angle),     
                x + radius * math.cos(j * angle),
                y - radius * math.sin(j * angle))     

turtle.speed(0) # Fastest   

drawPolygon(0, 0, 50, 6)

turtle.hideturtle()

turtle.done()