from tkinter import * # Import all definitions from tkinter

window = Tk()
label = Label(window , text = "Welcome to Python") # Create a "label
button = Button(window , text = "Click Me")  # Create a button
label.pack() # PI ace the "label in the window
button.pack() # Place the button in the window

window.mainloop() # Create an event loop
