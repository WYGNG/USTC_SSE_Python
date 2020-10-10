import turtle

x, y = eval(input("Enter the coordinates for the center of the circle: "))
radius = eval(input("Enter the radius of the circle: "))

turtle.goto(x, y)
turtle.write(radius * radius * 3.1415)

turtle.penup()
turtle.goto(x, y - radius)
turtle.pendown()
turtle.circle(radius)

turtle.hideturtle()

input("Press any key to exit...")