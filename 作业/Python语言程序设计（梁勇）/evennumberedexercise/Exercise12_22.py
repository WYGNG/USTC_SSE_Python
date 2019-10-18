from tkinter import * # Import tkinter

class CoinLabel(Label):
    def __init__(self, container, text):
        Label.__init__(self, container, 
                        text = text, font = "Helvetica 30 bold")
        self.bind("<Button-1>", self.flip)
      
    def flip(self, event):
        if self["text"] == "H":
            self["text"] = "T"    
        else:   
            self["text"] = "H"

class MainClass:
    def __init__(self):  
        window = Tk() # Create a window
        window.title("Flip Coin") # Set title
        
        frame = Frame(window)
        frame.pack()
        
        for i in range(3):
            for j in range(3):
                CoinLabel(frame, text = "H").grid(row = i, column = j)
        
        window.mainloop() # Create an event loop

MainClass()
