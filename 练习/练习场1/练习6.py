from tkinter import * # Import all definitions from tkinter
class MouseKeyEventDemo:
    def __init__(self):
        window = Tk() # Create a window
        window.title("Event Demo") # Set title
        canvas = Canvas(window , bg = "white" , width = 200 , height = 100)
        canvas.pack()

        canvas.bind("<Button-l>",self.processMouseEvent)

        canvas.bind("<Key>",self.processKeyEvent)
        canvas.focus_set()

        window. mainloop()

    def processMouseEvent(self,event):
        print("clicked at" , event.x , event.y)
        print("Position in the screen" , event.x_root , event.y_root)
        print("Which button is clicked?", event.num)

    def processKeyEvent(self,event):
        #print("keysym?"，event.keysym)
        #print("char? "，event.char)
        #print("keycode?"，event.keycode)


MouseKeyEventDemo()# Create GUI
