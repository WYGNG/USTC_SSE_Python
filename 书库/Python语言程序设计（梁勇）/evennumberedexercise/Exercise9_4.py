from tkinter import * # Import tkinter
    
class MainGUI:
    def __init__(self):
        window = Tk() # Create a window
        window.title("Display Rectangles") # Set title
        
        frame1 = Frame(window)
        frame1.pack()
        
        canvas = Canvas(frame1, width = 400, height = 250)
        canvas.pack()
        
        for i in range(20):
            canvas.create_rectangle(10 + i * 6, 10 + i * 6, 
                int(canvas["width"]) - 10 - i * 6, int(canvas["height"]) - 10 - i * 6)
        
        window.mainloop() # Create an event loop

MainGUI()