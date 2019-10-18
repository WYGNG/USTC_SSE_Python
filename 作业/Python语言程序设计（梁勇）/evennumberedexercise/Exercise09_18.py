from tkinter import * # Import tkinter

width = 200
height = 100

class MainGUI:
    def __init__(self):
        window = Tk() # Create a window
        window.title("Flashing Text") # Set a title
        
        sleepTime = 100
        canvas = Canvas(window, bg = "white", width = width, height = height)
        canvas.pack()
        
        on = True
        while True:
            if on:
                canvas.create_text(width / 2, height / 2, text = "Welcome", tags = "text")
            else:
                canvas.delete("text")
                
            on = not on  
            canvas.after(sleepTime) # Sleep for 100 milliseconds
            canvas.update()
        
        window.mainloop() # Create an event loop

MainGUI()
