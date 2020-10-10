from tkinter import * # Import tkinter
import math

width = 200
height = 200
pendulumRadius = 150
ballRadius = 10
leftAngle = 120
rightAngle = 60
        
class MainGUI:
    def __init__(self):
        window = Tk() # Create a window
        window.title("Pendulum") # Set a title
        
        self.canvas = Canvas(window, bg = "white", width = width, height = height)
        self.canvas.pack()
        
        self.angle = leftAngle # Start from leftAngle
        self.angleDelta = 1 # Swing interval
        delay = 100
        
        while True:
            self.canvas.delete("pendulum")
            self.displayPendulum()
            self.canvas.after(100) # Sleep for 100 milliseconds
            self.canvas.update() # Update canvas

        self.displayPendulum()

        window.mainloop() # Create an event loop

    def displayPendulum(self):
        x1 = width / 2;
        y1 = 20;
          
        if self.angle < rightAngle:
            self.angleDelta = 1 # Swing to the left
        elif self.angle > leftAngle:
            self.angleDelta = -1 # Swing to the right
          
        self.angle += self.angleDelta
        x = x1 + pendulumRadius * math.cos(math.radians(self.angle))
        y = y1 + pendulumRadius * math.sin(math.radians(self.angle))
          
        self.canvas.create_line(x1, y1, x, y, tags = "pendulum")
        self.canvas.create_oval(x1 - 2, y1 - 2, x1 + 2, y1 + 2, fill = "black", tags = "pendulum")
        self.canvas.create_oval(x - ballRadius, y - ballRadius, x + ballRadius, y + ballRadius,
            fill = "black", tags = "pendulum")  

MainGUI()
