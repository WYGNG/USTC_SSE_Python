import turtle

# Draw a line from (x1, y1) to (x2, y2)
def drawLine(x1, y1, x2, y2, color = "black", size = 1):
    turtle.color(color)
    turtle.pensize(size)
    turtle.penup()
    turtle.goto(x1, y1)
    turtle.pendown()
    turtle.goto(x2, y2)
