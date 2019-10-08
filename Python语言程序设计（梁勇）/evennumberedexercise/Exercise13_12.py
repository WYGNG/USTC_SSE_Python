import math

def main():
    side1, side2, side3 = eval(input("Enter three sides: "))
    
    try:
        triangle = Triangle(side1, side2, side3)
    except TriangleError as ex:
        print("These three sides", ex.getSide1(),  
            ex.getSide2(), ex.getSide3(), " cannot form a legal triangle.")
        
    color = input("Enter color: ")
    triangle.setColor(color);
    
    filled = eval(input("Enter 1/0 for filled (1: true, 0: false): "))
    
    isFilled = (filled == 1)
    triangle.setFilled(isFilled);

    print("The area is", triangle.getArea())
    print("The perimeter is", triangle.getPerimeter())
    print("Color is", triangle.getColor())
    print("Filled is", triangle.isFilled())

class GeometricObject:
    def __init__(self, color = "green", filled = True):
        self.__color = color
        self.__filled = filled

    def getColor(self):
        return self.__color

    def setColor(self, color):
        self.__color = color

    def isFilled(self):
        return self.__filled

    def setFilled(self, filled):
        self.__filled = filled
  
    def __str__(self):
        return "color: " + self.__color + \
            " and filled: " + str(self.__filled)

class TriangleError(RuntimeError):
    def __init__(self, side1, side2, side3):
         super().__init__()
         self.__side1 = side1
         self.__side2 = side2        
         self.__side3 = side3
    
    def getSide1(self):
        return self.__side1
    
    def getSide2(self):
        return self.__side2
    
    def getSide3(self):
        return self.__side3
         
class Triangle(GeometricObject):
    def __init__(self, side1, side2, side3):
        self.__side1 = side1
        self.__side2 = side2
        self.__side3 = side3
        GeometricObject.__init__(self)
        if not self.isLegal():
            raise TriangleError(side1, side2, side3)

    def isLegal(self):
        return self.__side1 + self.__side2 > self.__side3 and \
            self.__side2 + self.__side3 > self.__side1 and \
            self.__side1 + self.__side3 > self.__side2  
            
    def getSide1(self):
        return self.__side1

    def getSide2(self):
        return self.__side2
    
    def getSide3(self):
        return self.__side3

    def getArea(self):
        s = (self.__side1 + self.__side2 + self.__side3) / 2
        return math.sqrt(s * (s - self.__side1) * (s - self.__side2) * (s - self.__side3))

    def getPerimeter(self):
        return self.__side1 + self.__side2 + self.__side3

    def toString(self):
        # Implement it to return the three sides
        return "Triangle: __side1 = " + str(self.__side1) + " __side2 = " + \
            str(self.__side2) + " __side3 = " + str(self.__side3)

main()
