import turtle

radius = eval(input("Enter radius: "))

turtle.penup()
turtle.goto(-radius, 0)
turtle.pendown()
turtle.circle(radius) 

turtle.penup()
turtle.goto(-radius, -2 * radius)
turtle.pendown()
turtle.circle(radius) 

turtle.penup()
turtle.goto(radius, 0)
turtle.pendown()
turtle.circle(radius) 

turtle.penup()
turtle.goto(radius, -2 * radius)
turtle.pendown()
turtle.circle(radius) 

input("Press any key to exit...")