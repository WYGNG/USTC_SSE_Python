import turtle

radius = 50

for i in range(10):
    turtle.penup() # Pull the pen up
    turtle.goto(0, -radius)
    turtle.pendown() # Pull the pen down

    turtle.circle(radius)
    radius += 5

turtle.hideturtle()

turtle.done()
