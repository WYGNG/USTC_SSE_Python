from tkinter import * # Import all definitions from tkinter
class RadioButtonsAndButtons:
    def __init__(self):
        window = Tk() # Create a window
        window.title("Radio buttons and buttons") # Set title
        window.geometry('400x200')
        self.v = StringVar()

        l = tk.Label(window, bg='yellow', width=20, text='empty')
        l.pack()
        
#        self.width = 500 # Width of self. canvas
 #       self.canvas = Canvas(window, bg = "yellow",width = self.width, height = 200)
   #     self.canvas.pack()

        frame0 = Frame(window)
        frame0.pack()


        def Radiobutton(self):
            l.config(text='you have selected ' + var.get())
        
        R1=Radiobutton(frame0, text="Red", variable=self.v, value="Red", bg = "Red",command=Radiobutton)
        R1.grid(row = 1, column = 1)
        R2=Radiobutton(frame0, text="Yellow", variable=self.v, value="Yellow",bg="Yellow", command=Radiobutton)
        R2.grid(row = 1, column = 2)
        R3=Radiobutton(frame0, text="White", variable=self.v, value="White",bg="White", command=Radiobutton)
        R3.grid(row = 1, column = 3)
        R4=Radiobutton(frame0, text="Gray", variable=self.v, value="Gray",bg="Gray", command=Radiobutton)
        R4.grid(row = 1, column = 4)
        R5=Radiobutton(frame0, text="Green", variable=self.v, value="Green",bg="Green", command=Radiobutton)
        R5.grid(row = 1, column = 5)

        
        self.x = 250 # Starting x position
   #     self.canvas.create_label(self.x , 100,text = "Welcome", tags = "text")


        self.dx = 10
        


            
        frame1 = Frame(window)
        frame1.pack()

        
        btLeft = Button(frame1 , text = " <= ", command = self.left)
        btLeft.pack(side = LEFT)
        btRight = Button(frame1, text = " => ",command = self.right)
        btRight.pack(side = RIGHT)




        


    def left(self): # 
        self.label.move("text", -self.dx, 0)

    def right(self): # 
        self.label.move("text", self.dx, 0)

        
        window.mainloop() # Create an event "loop


RadioButtonsAndButtons()
