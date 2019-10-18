# OOP Geometry Demo

class Point():
    x = 0.0
    y = 0.0

    def __init__(self, x, y):
        self.x = x
        self.y = y
        print("Point constructor")

    def ToString(self):
        return "{X:" + str(self.x) + ",Y:" + str(self.y) + "}"

class Size():
    width = 0.0
    height = 0.0

    def __init__(self,width,height):
        self.width = width
        self.height = height
        print("Size constructor")

    def ToString(self):
        return "{WIDTH=" + str(self.width) + \
               ",HEIGHT=" + str(self.height) + "}"

class Circle(Point):
    radius = 0.0

    def __init__(self, x, y, radius):
        super().__init__(x,y)
        self.radius = radius
        print("Circle constructor")

    def ToString(self):
        return super().ToString() + \
               ",{RADIUS=" + str(self.radius) + "}"

class Rectangle(Point,Size):
    def __init__(self, x, y, width, height):
        Point.__init__(self,x,y)
        Size.__init__(self,width,height)
        print("Rectangle constructor")

    def ToString(self):
        return Point.ToString(self) + "," + Size.ToString(self)
        

p = Point(10,20)
print(p.ToString())

s = Size(80,70)
print(s.ToString())

c = Circle(100,100,50)
print(c.ToString())

r = Rectangle(200,250,40,50)
print(r.ToString())
