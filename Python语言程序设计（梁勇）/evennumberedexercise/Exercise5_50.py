import turtle

x = -100
y = 100
line = ""
for i in range(1, 12):
    for j in range(1, i):
        line += str(j) + " "
    
    # Draw a line
    turtle.penup() # Pull the pen up
    turtle.goto(x, y)
    turtle.pendown() # Pull the pen down
    turtle.write(line, font = ("Times", 18, "bold"))

    line = ""
    y -= 20

turtle.hideturtle()

turtle.done()