from tkinter import *
class ProcessButtonEvent:
    def __int__(self):
        window = Tk()
        window.title("Contro1 Animation Demo") # Set title


        self.width = 250 # Width of self. canvas
        self.canvas = Canvas(window, bg = "yellow",width = self.width, height = 50)
        self.canvas.pack()

        frame1 = Frame(window)
        frame1.pack()
        
        btOk = Button(window,text = "Ok",fg = "red",command = self.processOk)
        btCancle = Button(window,text= "Cancle",fg = "yellow",command = self.processCancleprocessCancle)
        btOk.pack()
        btCancle.pack()
        window.mainloop()
    def processOk(self):
        print("Ok button is clicked")
    def processCancle(self):
        print("Canlce button is clicked")
        
ProcessButtonEvent()
