import turtle

turtle.pensize(3) # Set pen thickness to 3 pixels
turtle.penup() # Pull the pen up
turtle.goto(-200, -50)
turtle.setheading(60)
turtle.pendown() # Pull the pen down
turtle.begin_fill() # Begin to fill color in a shape
turtle.color("red")
turtle.circle(40, steps = 3) # Draw a triangle
turtle.end_fill() # Fill the shape

turtle.penup()
turtle.goto(-100, -50)
turtle.pendown()
turtle.begin_fill() # Begin to fill color in a shape
turtle.color("blue")
turtle.setheading(45)
turtle.circle(40, steps = 4) # Draw a square
turtle.end_fill() # Fill the shape

turtle.penup()
turtle.goto(0, -50)
turtle.pendown()
turtle.begin_fill() # Begin to fill color in a shape
turtle.color("green")
turtle.setheading(35)
turtle.circle(40, steps = 5) # Draw a pentagon
turtle.end_fill() # Fill the shape

turtle.penup()
turtle.goto(100, -50)
turtle.pendown()
turtle.begin_fill() # Begin to fill color in a shape
turtle.color("yellow")
turtle.setheading(30)
turtle.circle(40, steps = 6) # Draw a hexagon
turtle.end_fill() # Fill the shape

turtle.penup()
turtle.goto(200, -50)
turtle.pendown()
turtle.begin_fill() # Begin to fill color in a shape
turtle.color("purple")
turtle.setheading(25)
turtle.circle(40, steps = 8) # Draw a circle
turtle.end_fill() # Fill the shape

turtle.color("green")
turtle.penup()
turtle.goto(-100, 50)
turtle.pendown()
turtle.write("Cool Colorful Shapes", 
  font = ("Times", 18, "bold"))
turtle.hideturtle()

turtle.done()
