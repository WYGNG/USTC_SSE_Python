from tkinter import * # Import tkinter
import tkinter.messagebox
import random 

width = 340
height = 150
radius = 2
        
class MainGUI:
    def __init__(self):
        window = Tk() # Create a window
        window.title("Insertion Sort Animation") # Set title
        
        self.canvas = Canvas(window, width = width, height = height)
        self.canvas.pack()
        
        frame = Frame(window)
        frame.pack()
        
        Button(frame, text = "Step", command = self.step).pack(side = LEFT)
        Button(frame, text = "Reset", command = self.reset).pack(side = LEFT)

        self.list = [ x for x in range(1, 20) ]
        self.reset()
        self.key = 0
        
        self.drawAStep()
        
        window.mainloop() # Create an event loop
        
    def reset(self):       
        self.i = 0 # current index 
        self.done = False
        random.shuffle(self.list)
        self.drawAStep()

    def step(self):
        if self.i > len(self.list) - 1:
            tkinter.messagebox.showinfo("showinfo", "The list is already sorted")
            return
              
        # insert list[i] into a sorted sublist list[0..i-1] so that
        #list[0..i] is sorted. */
        currentElement = self.list[self.i]
        k = self.i - 1
        while k >= 0 and self.list[k] > currentElement:
            self.list[k + 1] = self.list[k]
            k -= 1
            
        # Insert the current element into list[k + 1]
        self.list[k + 1] = currentElement

        self.drawAStep()
        self.i += 1 # Increase step
        
    def drawAStep(self):
        bottomGap = 10
        self.canvas.delete("line")
        self.canvas.create_line(10, height - bottomGap, width - 10, height - bottomGap, tag = "line")
        barWidth = (width - 20) / len(self.list)
        
        maxCount = int(max(self.list))
        for i in range(len(self.list)):
            self.canvas.create_rectangle(i * barWidth + 10, (height - bottomGap) * (1 - self.list[i] / (maxCount + 4)), 
                (i + 1) * barWidth + 10, height - bottomGap, tag = "line")       
                         
            self.canvas.create_text(i * barWidth + 10 + barWidth / 2, (height - bottomGap) * ( 1 - self.list[i] / (maxCount + 4)) - 8, 
                               text = str(self.list[i]), tag = "line")

        if self.i >= 0:
            self.canvas.create_rectangle(self.i * barWidth + 10, (height - bottomGap) * ( 1 - self.list[self.i] / (maxCount + 4)), 
                                    (self.i + 1) * barWidth + 10, height - bottomGap, fill = "red", tag = "line")

MainGUI()
