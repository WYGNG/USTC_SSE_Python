import turtle
import math
from UsefulTurtleFunctions import drawLine
from UsefulTurtleFunctions import writeText

turtle.speed(0) # Fastest   

# Draw a square function
scaleFactor = 0.01
left = -100
right = 100
x = left
turtle.penup()
turtle.goto(x, scaleFactor * x * x)
turtle.pendown()
for  x in range(left, right + 1):
    turtle.goto(x, scaleFactor * x * x)

# Draw X-axis
drawLine(-160, 0, 160, 0)

# Draw Y-axis
drawLine(0, -80, 0, 80)

# Display X
writeText("Y", 0, 80)
            
# Display Y
writeText("X", 180, -15) 

# Draw arrows
turtle.degrees()
turtle.penup()
turtle.goto(160, 0)
turtle.pendown()
turtle.setheading(150)
turtle.forward(20)

turtle.penup()
turtle.goto(160, 0)
turtle.pendown()
turtle.setheading(-150)
turtle.forward(20)

turtle.penup()
turtle.goto(0, 80)
turtle.pendown()
turtle.setheading(240)
turtle.forward(20)

turtle.penup()
turtle.goto(0, 80)
turtle.pendown()
turtle.setheading(-60)
turtle.forward(20)

turtle.hideturtle()

turtle.done()