import turtle
import math

x1, y1, x2, y2, x3, y3 = eval(input("Enter three points for a triangle: "))

a = math.sqrt((x2 - x3) * (x2 - x3) + (y2 - y3) * (y2 - y3))
b = math.sqrt((x1 - x3) * (x1 - x3) + (y1 - y3) * (y1 - y3))
c = math.sqrt((x1 - x2) * (x1 - x2) + (y1 - y2) * (y1 - y2))

A = math.degrees(math.acos((a * a - b * b - c * c) / (-2 * b * c)))
B = math.degrees(math.acos((b * b - a * a - c * c) / (-2 * a * c)))
C = math.degrees(math.acos((c * c - b * b - a * a) / (-2 * a * b)))

turtle.penup()
turtle.goto(x1, y1)
turtle.pendown()
turtle.write("p1 (" + "{0:0.2f}".format(A) + ")")
turtle.goto(x2, y2)
turtle.write("p2 (" + "{0:0.2f}".format(B) + ")")
turtle.goto(x3, y3)
turtle.write("p3 (" + "{0:0.2f}".format(C) + ")")
turtle.goto(x1, y1)

turtle.hideturtle()

turtle.done()