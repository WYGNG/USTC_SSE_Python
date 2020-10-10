import math

def main():
    numberOfSides = eval(input("Enter the number of sides: "))
    side = eval(input("Enter the side: "))
    
    print("The area of the polygon is " + str(area(numberOfSides, side)))
  
def area(n, side):
    return n * side * side / math.tan(math.pi / n) / 4

main()