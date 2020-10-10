import math

side = eval(input("Enter the side: "))
# Compute the area
area = 5 * side * side / math.tan(math.pi / 5) / 4

print("The area of the pentagon is " + str(area))