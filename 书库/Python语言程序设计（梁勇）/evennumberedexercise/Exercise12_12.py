from tkinter import * # Import tkinter
from StillClock import StillClock   
    
window = Tk() # Create a window
window.title("Display Clocks") # Set title

clock1 = StillClock(window) 
clock1.grid(row = 1, column = 1)

clock2 = StillClock(window) 
clock2.grid(row = 1, column = 2)

clock3 = StillClock(window) 
clock3.grid(row = 1, column = 3)

clock4 = StillClock(window) 
clock4.grid(row = 1, column = 4)

window.mainloop() # Create an event loop
