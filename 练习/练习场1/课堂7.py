from tkinter import * # Import all definitions from tkinter
class ControlAnimation:
    def __init__(self):
        window = Tk() # Create a window
        window.title("Contro1 Animation Demo") # Set title

        self.width = 250 # Width of self. canvas
        self.canvas = Canvas(window, bg = "white",width = self.width, height = 50)
        self.canvas.pack()

        frame = Frame(window)
        frame.pack()
        btStop = Button(frame , text = "Stop", command = self. stop)
        btStop.pack(side = LEFT)
        btResume = Button(frame, text = "Resume",
        command = self. resume)
        btResume. pack(side = LEFT)
        btFaster = Button(frame, text = "Faster" ,
        command = self.faster)
        btFaster.pack(side = LEFT)
        btSlower = Button(frame, text = "Slower",
        command = self.slower)
        btSlower.pack(side = LEFT)

        self.x = 0 # Starting x position
        self.sleepTime = 100 # Set a sleep time
        self.canvas. create_text(self. x , 30,
            text = "Welcome", tags = "text")

        self.dx = 3
        self.isStopped = False
        self.animate()

        window.mainloop() # Create an event "loop

    def stop(self): # Stop animation
        self.isStopped = True

    def resume(self): # Resume animation
        self.isStopped = False
        self.animate()

    def faster(self): # Speed up the animation
        if self.sleepTime > 5:
            self.sleepTime -= 20

    def slower(self): # Slow down the animation
        self.sleepTime += 20

    def animate(self): # Move the message
        while not self.isStopped:
            self.canvas.move("text", self.dx, 0) # Move text
            self.canvas.after(self. sleepTime) # Sleep
            self.canvas.update() # Update canvas
            if self.x < self.width:
                self.x += self.dx # Set new position
            else:
                self.x = 0 # Reset string position to beginning
                self.canvas.delete("text")
                self.canvas.create_text (self.x , 30 ,
                    text = "Welcome" , tags = "text")
    # Redraw text at the beginning
ControlAnimation()
