import turtle
import math
from UsefulTurtleFunctions import drawLine
from UsefulTurtleFunctions import writeText

turtle.speed(0) # Fastest   

# Draw X-axis
drawLine(-220, 0, 220, 0)

# Draw arrows
turtle.degrees()
turtle.setheading(150)
turtle.forward(20)

turtle.penup()
turtle.goto(220, 0)
turtle.pendown()
turtle.setheading(-150)
turtle.forward(20)

# Draw Y-axis
drawLine(0, -80, 0, 80)

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

# Draw sine function
x = -175
turtle.penup()
turtle.goto(x, 50 * math.sin((x / 100.0) * 2 * math.pi))
turtle.pendown()

for x in range(-175, 176): 
    turtle.goto(x, 50 * math.sin((x / 100.0) * 2 * math.pi))

writeText("-2\u03c0", -100, -15)
writeText("2\u03c0", 100, -15)

turtle.hideturtle()

turtle.done()