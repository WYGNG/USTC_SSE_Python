from tkinter import * # Import tkinter

class MainGUI:
    def __init__(self):
        coordinates = input("Enter coordinates for six points separated by spaces: ")
        c = coordinates.split()
        points = [[eval(c[i]), eval(c[i + 1])] for i in range(0, len(c), 2)]
        
        window = Tk() # Create a window
        window.title("Polygon") # Set title
        
        width = 400
        height = 250
        canvas = Canvas(window, width = width, height = height)
        canvas.pack()
                
        canvas.create_polygon(points)        
        
        window.mainloop() # Create an event loop
        
MainGUI()
