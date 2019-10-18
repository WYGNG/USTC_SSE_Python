import math

def main():
    x1, y1, radius1 = eval(input("Enter x1, y1, radius1: "))
    x2, y2, radius2 = eval(input("Enter x2, y2, radius2: "))
    c1 = Circle2D(x1, y1, radius1)
    c2 = Circle2D(x2, y2, radius2)
    
    print("Area for c1 is", c1.getArea())
    print("Perimeter for c1 is", c1.getPerimeter())
    
    print("Area for c2 is", c2.getArea())
    print("Perimeter for c2 is", c2.getPerimeter())
    
    print("c1 contains the center of c2?", c1.containsPoint(c2.getX(), c2.getY()))
    print("c1 contains c2?", c1.contains(c2))
    print("c2 in c1?", c2 in c1)
    print("c1 overlaps c2?", c1.overlaps(c2))

    print("c1 < c2?", c1 < c2)
    
class Circle2D:
    def __init__(self, x = 0, y = 0, radius = 0):
        self.__x = x
        self.__y = y
        self.__radius = radius

    def getX(self):
        return self.__x

    def getY(self):
        return self.__y

    def getRadius(self):
        return self.__radius
    
    def setX(self, x):
        self.__x = x
        
    def setY(self, y):
        self.__y = y

    def setRadius(self, radius):
        self.__radius = radius
  
    def getPerimeter(self):
        return 2 * self.__radius * math.pi

    def getArea(self):
        return self.__radius * self.__radius * math.pi
  
    def containsPoint(self, x, y):
        d = distance(x, y, self.__x, self.__y)
        return d <= self.__radius

    def contains(self, circle):
        d = distance(self.__x, self.__y, circle.__x, circle.__y)
        return d + circle.__radius <= self.__radius
  
    def overlaps(self, circle):
        return distance(self.__x, self.__y, circle.__x, circle.__y) \
            <= self.__radius + circle.__radius

    def __contains__(self, anotherCircle):
        return self.contains(anotherCircle)

    def __lt__(self, secondCircle): 
        return self.__cmp__(secondCircle) < 0

    def __le__(self, secondCircle): 
        return self.__cmp__(secondCircle) <= 0

    def __gt__(self, secondCircle): 
        return self.__cmp__(secondCircle) > 0

    def __ge__(self, secondCircle): 
        return self.__cmp__(secondCircle) >= 0
   
    # Compare two numbers
    def __cmp__(self, secondCircle): 
        if self.__radius > secondCircle.__radius:
            return 1
        elif self.__radius < secondCircle.__radius:
            return -1
        else:
            return 0        
        
def distance(x1, y1, x2, y2):
    return math.sqrt((x1 - x2) * (x1 - x2) + (y1 - y2) * (y1 - y2))

main()
