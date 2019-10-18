from tkinter import * # Import tkinter
    
class MainGUI:
    def computeFutureValue(self):
        monthlyInterestRate = float(self.annualInterestRate.get()) / 1200
        f = float(self.investmentAmount.get()) * \
            (1 + monthlyInterestRate) ** (float(self.numberOfYears.get()) * 12)
        self.futureValue.set("{0:10.2f}".format(f))

    def __init__(self):
        window = Tk() # Create a window
        window.title("Investment Calculator") # Set title
        
        Label(window, text = "Investment Amount").grid(row = 1, 
            column = 1, sticky = W)
        Label(window, text = "Years").grid(row = 2, 
            column = 1, sticky = W)
        Label(window, text = "Annual Interest Rate").grid(row = 3, 
            column = 1, sticky = W)
        Label(window, text = "Future Value").grid(row = 4, 
            column = 1, sticky = W)
        
        self.investmentAmount = StringVar()
        Entry(window, textvariable = self.investmentAmount, 
            justify = RIGHT).grid(row = 1, column = 2)
        self.annualInterestRate = StringVar()
        Entry(window, textvariable = self.annualInterestRate, 
            justify = RIGHT).grid(row = 3, column = 2)
        self.numberOfYears = StringVar()
        Entry(window, textvariable = self.numberOfYears, 
            justify = RIGHT).grid(row = 2, column = 2)
        self.futureValue = StringVar()
        Label(window, textvariable = 
            self.futureValue).grid(row = 4, column = 2, sticky = E)
            
        Button(window, text = "Calculate", 
            command = self.computeFutureValue).grid(row = 6, column = 2, sticky = E)
        
        window.mainloop() # Create an event loop

MainGUI()
