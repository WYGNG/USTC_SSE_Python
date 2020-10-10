import turtle
import math

# Fill a rectangle 
def drawRectangle(color = "black", 
                  x = 0, y = 0, width = 30, height = 30): 
    turtle.color(color)
    turtle.begin_fill() # Begin to fill color in a shape
    
    turtle.penup() # Pull the pen up
    turtle.goto(x + width / 2, y + height / 2)
    turtle.pendown() # Pull the pen down
    turtle.right(90)
    turtle.forward(height)
    turtle.right(90)
    turtle.forward(width)
    turtle.right(90)
    turtle.forward(height)
    turtle.right(90)
    turtle.forward(width)
    
    turtle.end_fill() # Fill the shape
        
# Fill a circle
def drawCircle(color = "black", x = 0, y = 0, radius = 50): 
    turtle.color(color)
    turtle.penup() # Pull the pen up
    turtle.goto(x, y)
    turtle.pendown() # Pull the pen down
    turtle.begin_fill() # Begin to fill color in a shape
    turtle.circle(radius) 
    turtle.end_fill() # Fill the shape
    