import turtle
import math
from UsefulTurtleFunctions import drawLine

# Draw a snow flak with the specified order on one line
def displayKochSnowFlake(order, p1, p2):
    if order == 0:
        # Draw a line
        drawLine(p1, p2)
    else:
        # Get points x, y, z on the edge 
        deltaX = p2[0] - p1[0]
        deltaY = p2[1] - p1[1]

        x = [p1[0] + deltaX / 3, p1[1] + deltaY / 3]
        y = [p1[0] + deltaX * 2 / 3, p1[1] + deltaY * 2 / 3]
        z = [((p1[0] + p2[0]) / 2 - math.cos(math.radians(30)) * (p1[1] - p2[1]) / 3),
          (int)((p1[1] + p2[1]) / 2 - math.cos(math.radians(30)) * (p2[0] - p1[0]) / 3)]

        # Recursively display snow flakes on lines
        displayKochSnowFlake(order - 1, p1, x)
        displayKochSnowFlake(order - 1, x, z)
        displayKochSnowFlake(order - 1, z, y)
        displayKochSnowFlake(order - 1, y, p2)
    
# Return the midpoint between two points
def midpoint(p1, p2):
    p = 2 * [0]
    p[0] = (p1[0] + p2[0]) / 2
    p[1] = (p1[1] + p2[1]) / 2
    return p

def main():
    p1 = [0, 175]
    p2 = [-150, -75]
    p3 = [150, -75]

    order = eval(input("Enter an order: "))
    displayKochSnowFlake(order, p1, p2)
    displayKochSnowFlake(order, p2, p3)
    displayKochSnowFlake(order, p3, p1)

    turtle.done()

main()
