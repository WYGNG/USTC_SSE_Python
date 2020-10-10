# Enter radius of the cylinder
radius, length  = eval(input("Enter the radius and length of a cylinder: "))

area = radius * radius * 3.14159
volume = area * length

print("The area is " + str(area))
print("The volume of the cylinder is " + str(volume))