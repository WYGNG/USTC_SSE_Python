def main():
    items = input("Enter the points: ").strip().split()
    
    points = [[eval(items[i]), eval(items[i + 1])] for i in range(0, len(items), 2)]
    
    r = getRectangle(points)
    
    print("The bounding rectangle is centered at (" + str(r.getX()) + ", " + str(r.getY()) + \
          ") with width " + str(r.getWidth()) + " and height " + str(r.getHeight()))

def getRectangle(points): 
    minX = getMinX(points)
    minY = getMinY(points)
    maxX = getMaxX(points)
    maxY = getMaxY(points)
    
    return Rectangle2D( (minX + maxX) / 2, (minY + maxY) / 2, maxX - minX, maxY - minY)
      
def getMinX(points):
    minX = points[0][0]
    
    for i in range(len(points)):
        if minX > points[i][0]:
            minX = points[i][0]
    
    return minX
      
def getMaxX(points):
    maxX = points[0][0]
    
    for i in range(len(points)):
        if maxX < points[i][0]:
            maxX = points[i][0]
    
    return maxX

def getMinY(points):
    minY = points[0][1]
    
    for i in range(len(points)):
        if minY > points[i][1]:
            minY = points[i][1]
    
    return minY

def getMaxY(points):
    maxY = points[0][1]
    
    for i in range(len(points)):
        if maxY < points[i][1]:
            maxY = points[i][1]
    
    return maxY

class Rectangle2D:
    def __init__(self, x = 0, y = 0, width = 0, height = 0):
        self.x = x
        self.y = y
        self.width = width
        self.height = height

    def getX(self):
        return self.x

    def getY(self):
        return self.y

    def getWidth(self):
        return self.width
    
    def getHeight(self):
        return self.height

    def setHeight(self, x):
        self.x = x

    def setHeight(self, y):
        self.y = y

    def setWidth(self, width):
        self.width = width

    def setHeight(self, height):
        self.height = height

    def getPerimeter(self):
        return 2 * (self.width + self.height)
  
    def getArea(self):
        return self.width * self.height
  
    def containsPoint(self, x, y):
        return abs(x - self.x) <= self.width / 2 and abs(y - self.y) <= self.height / 2
  
    def contains(self, r):    
        return self.containsPoint(r.x - r.width / 2, r.y + r.height / 2) and \
            self.containsPoint(r.x - r.width / 2, r.y - r.height / 2) and \
            self.containsPoint(r.x + r.width / 2, r.y + r.height / 2) and \
            self.containsPoint(r.x + r.width / 2, r.y - r.height / 2)
  
    def overlaps(self, r):  
        return abs(self.x - r.x) <= (self.width + r.width) / 2 and \
            abs(self.y - r.y) <= (self.height + r.height) / 2 
            
main()
