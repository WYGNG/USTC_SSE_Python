from tkinter import * # Import all definitions from tkinter
class PlaceManagerDemo:
    def __init__(self):
        window = Tk() # Create a window
        window.title("Place Manager Demo") # Set title
        Label(window , text = "USTC_SSE" , bg = "yellow").place (x = 20, y = 20)
        Label(window , text = "SA19225404" , bg = "Red").place(x = 50 , y = 50)
        Label(window , text = "吴语港" , bg = "green").place (x = 80 , y = 80)

        window.mainloop() # Create an event loop

PlaceManagerDemo() # Create GUI
