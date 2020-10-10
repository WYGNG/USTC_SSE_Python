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
        c1x.set(c1.getX())
        c1y.set(c1.getY())
        c1Radius.set(c1.getRadius())
        if c1.overlaps(c2):
            label["text"] = "Two circles intersect"
        else:
            label["text"] = "Two circles don't intersect"
    elif c2.containsPoint(event.x, event.y):
        c2.setX(event.x)
        c2.setY(event.y)
        displayCircle(c2, "c2")
        c2x.set(c2.getX())
        c2y.set(c2.getY())
        c2Radius.set(c2.getRadius())
        if c1.overlaps(c2):
            label["text"] = "Two circles intersect"
        else:
            label["text"] = "Two circles don't intersect"

def redraw():
    c1.x = c1x.get()
    c1.y = c1y.get()
    c1.radius = c1Radius.get()
    c2.x = c2x.get()
    c2.y = c2y.get()
    c2.radius = c2Radius.get()
    displayCircle(c1, "c1")
    displayCircle(c2, "c2")    
    
window = Tk() # Create a window
window.title("Two Circles") # Set title

width = 250
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

frame1 = Frame(window)
frame1.pack()
Label(frame1, text = "C1 Center x:").grid(row = 1, column = 1)
Label(frame1, text = "C1 Center y:").grid(row = 2, column = 1)
Label(frame1, text = "C1 Radius:").grid(row = 3, column = 1)

c1x = DoubleVar()
c1x.set(c1.x)
Entry(frame1, width = 5, justify = RIGHT, textvariable = c1x).grid(row = 1, column = 2)

c1y = DoubleVar()
c1y.set(c1.y)
Entry(frame1, width = 5, justify = RIGHT, textvariable = c1y).grid(row = 2, column = 2)

c1Radius = DoubleVar()
c1Radius.set(c1.radius)
Entry(frame1, width = 5, justify = RIGHT, textvariable = c1Radius).grid(row = 3, column = 2)

Label(frame1, text = "C2 Center x:").grid(row = 1, column = 3)
Label(frame1, text = "C2 Center y:").grid(row = 2, column = 3)
Label(frame1, text = "C2 Radius:").grid(row = 3, column = 3)

c2x = DoubleVar()
c2x.set(c2.x)
Entry(frame1, width = 5, justify = RIGHT, textvariable = c2x).grid(row = 1, column = 4)

c2y = DoubleVar()
c2y.set(c2.y)
Entry(frame1, width = 5, justify = RIGHT, textvariable = c2y).grid(row = 2, column = 4)

c2Radius = DoubleVar()
c2Radius.set(c2.radius)
Entry(frame1, width = 5, justify = RIGHT, textvariable = c2Radius).grid(row = 3, column = 4)

frame2 = Frame(window)
frame2.pack()
Button(frame2, text = "Redraw Circles", command = redraw).pack()

window.mainloop() # Create an event loop
