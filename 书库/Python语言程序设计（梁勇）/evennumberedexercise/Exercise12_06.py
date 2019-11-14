from tkinter import * # Import tkinter
import math

class Circle2D:
    def __init__(self, x = 0, y = 0, radius = 0):
        self.x = x
        self.y = y
        self.radius = radius

    def getX(self):
        return self.x

    def getY(self):
        return self.y

    def getRadius(self):
        return self.radius
    
    def setX(self, x):
        self.x = x
        
    def setY(self, y):
        self.y = y

    def setRadius(self, radius):
        self.radius = radius
  
    def getPerimeter(self):
        return 2 * self.radius * math.pi

    def getArea(self):
        return self.radius * self.radius * math.pi
  
    def containsPoint(self, x, y):
        d = distance(x, y, self.x, self.y)
        return d <= self.radius

    def contains(self, circle):
        d = distance(self.x, self.y, circle.x, circle.y)
        return d + circle.radius <= self.radius
  
    def overlaps(self, circle):
        return distance(self.x, self.y, circle.x, circle.y) \
            <= self.radius + circle.radius

def distance(x1, y1, x2, y2):
    return math.sqrt((x1 - x2) * (x1 - x2) + (y1 - y2) * (y1 - y2))

def displayCircle(c, text):
    canvas.delete(text)
    canvas.create_oval(c.x - c.radius,  
        c.y - c.radius, c.x + c.radius, c.y + c.radius, tags = text)
    canvas.create_text(c.x, c.y, text = text, tags = text)
            
def mouseMoved(event):
    if c1.containsPoint(event.x, event.y):
        c1.setX(event.x)
        c1.setY(event.y)
        displayCircle(c1, "c1")
        if c1.overlaps(c2):
            label["text"] = "Two circles intersect"
        else:
            label["text"] = "Two circles don't intersect"
    elif c2.containsPoint(event.x, event.y):
        c2.setX(event.x)
        c2.setY(event.y)
        displayCircle(c2, "c2")
        if c1.overlaps(c2):
            label["text"] = "Two circles intersect"
        else:
            label["text"] = "Two circles don't intersect"
            
window = Tk() # Create a window
window.title("Two Circles") # Set title

width = 300
height = 100
label = Label(window, text = "Two circles intersect" )
label.pack()
canvas = Canvas(window, width = width, height = height)
canvas.pack()

canvas.bind("<B1-Motion>", mouseMoved)
c1 = Circle2D(10, 10, 30)
c2 = Circle2D(30, 40, 20)
displayCircle(c1, "c1")
displayCircle(c2, "c2")

window.mainloop() # Create an event loop
