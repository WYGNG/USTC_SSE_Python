import math

x1, y1 = eval(input("Enter point 1 (latitude and longitude) in degrees: "))
x2, y2 = eval(input("Enter point 2 (latitude and longitude) in degrees: "))

d = 6371.01 * math.acos(math.sin(math.radians(x1)) * math.sin(math.radians(x2)) +
      math.cos(math.radians(x1)) * math.cos(math.radians(x2)) * 
      math.cos(math.radians(y1 - y2)));

print("The distance between the two points is", d, "km")
