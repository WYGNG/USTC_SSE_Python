import turtle

length = eval(input("Enter the length of a star: "))
              
turtle.penup()
turtle.goto(0, length / 2)
turtle.pendown()

turtle.right(72)
turtle.forward(length)

turtle.right(144)
turtle.forward(length)

turtle.right(144)
turtle.forward(length)

turtle.right(144)
turtle.forward(length)

turtle.right(144)
turtle.forward(length)

turtle.done()
