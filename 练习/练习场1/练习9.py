import tkinter as tk

window = tk.Tk()
window.title('Radio buttons and buttons')
window.geometry('500x250')

var = tk.StringVar()
l = tk.Label(window, bg = 'yellow', width = 20, text = 'Welcome')
lx = 180

def selection():
    l.config(bg = var.get())
    
def left(): # 
    global lx 
    lx = lx - 40
    l.place(x = lx,y = 100)

def right(): # 
    global lx 
    lx = lx + 40
    l.place(x = lx,y = 100)
    
r1 = tk.Radiobutton(window, text='Red',
                    variable=var, value='Red',
                    command=selection)
r1.place(x = 0,y = 0)
r2 = tk.Radiobutton(window, text='Yellow',
                    variable=var, value='Yellow',
                    command=selection)
r2.place(x = 100,y = 0)
r3 = tk.Radiobutton(window, text='White',
                    variable=var, value='White',
                    command=selection)
r3.place(x = 200,y = 0)
r4 = tk.Radiobutton(window, text='Gray',
                    variable=var, value='Gray',
                    command=selection)
r4.place(x = 300,y = 0)
r5 = tk.Radiobutton(window, text='Green',
                    variable=var, value='Green',
                    command=selection)
r5.place(x = 400,y = 0)

l.place(x = lx,y = 100)

        
bl = tk.Button(window , text = " <= ",width = 8, command = left)
bl.place(x = 175,y = 200)
br = tk.Button(window, text = " => ",width = 8,command = right)
br.place(x = 275,y = 200)


    
window.mainloop()
