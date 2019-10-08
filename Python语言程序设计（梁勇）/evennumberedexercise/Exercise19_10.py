from tkinter import * # Import tkinter
import tkinter.messagebox
from BinaryTree import BinaryTree 

class Heap:
    def __init__(self):
        self.lst = []

    # Add a new item into the lst 
    def add(self, e):
        self.lst.append(e)  # Append to the lst
        # The index of the last node
        currentIndex = len(self.lst) - 1  
    
        while currentIndex > 0:
            parentIndex = (currentIndex - 1) // 2
            # Swap if the current item is greater than its parent
            if self.lst[currentIndex] > self.lst[parentIndex]: 
               self.lst[currentIndex], self.lst[parentIndex] = \
                   self.lst[parentIndex], self.lst[currentIndex]
            else:
                break  # The tree is a lst now
    
            currentIndex = parentIndex

    # Remove the root from the lst 
    def remove(self):
        if len(self.lst) == 0:
           return None
    
        removedItem = self.lst[0]
        self.lst[0] = self.lst[len(self.lst) - 1]
        self.lst.pop(len(self.lst) - 1) # Remove the last item
    
        currentIndex = 0
        while currentIndex < len(self.lst):
            leftChildIndex = 2 * currentIndex + 1
            rightChildIndex = 2 * currentIndex + 2
          
            # Find the maximum between two children
            if leftChildIndex >= len(self.lst): 
                break  # The tree is a lst
            maxIndex = leftChildIndex
            if rightChildIndex < len(self.lst):
                if self.lst[maxIndex] < self.lst[rightChildIndex]:
                    maxIndex = rightChildIndex
          
            # Swap if the current node is less than the maximum 
            if self.lst[currentIndex] < self.lst[maxIndex]:
                self.lst[maxIndex], self.lst[currentIndex] = \
                    self.lst[currentIndex], self.lst[maxIndex]
                currentIndex = maxIndex
            else:
                break  # The tree is a lst
    
        return removedItem
  
    # Returns the size of the heap.
    def getSize(self):
        return len(self.lst)

def insert():
    k = int(key.get())
    heap.add(k) # Insert a new key
    canvas.delete("tree")
    displayTree(0, width / 2, 30, width / 4)

def delete():
    heap.remove() 
    canvas.delete("tree")
    displayTree(0, width / 2, 30, width / 4)

# Display a subtree rooted at position (x, y)
def displayTree(index, x, y, hGap):
    if index < heap.getSize():
        # Display the root
        canvas.create_oval(x - radius, y - radius,
                           x + radius, y + radius, tags = "tree")
        canvas.create_text(x, y, 
                           text = str(heap.lst[index]), tags = "tree")
     
        # Draw a line to the left node
        indexOfLeft = 2 * index + 1
        if indexOfLeft < heap.getSize():
            connectTwoCircles(x - hGap, y + vGap, x, y)
            
        # Draw the left subtree
        displayTree(indexOfLeft, x - hGap, y + vGap, hGap / 2)
          
        # Draw a line to the right node
        indexOfRight = 2 * index + 2        
        if indexOfRight < heap.getSize():
            connectTwoCircles(x + hGap, y + vGap, x, y)
            
        # Draw the right subtree
        displayTree(indexOfRight, x + hGap, y + vGap, hGap / 2)
                
# Connect two circles centered at (x1, y1) and (x2, y2) 
def connectTwoCircles(x1, y1, x2, y2):
    d = (vGap * vGap + (x2 - x1) * (x2 - x1)) ** 0.5
    x11 = x1 - radius * (x1 - x2) / d
    y11 = y1 - radius * (y1 - y2) / d
    x21 = x2 + radius * (x1 - x2) / d
    y21 = y2 + radius * (y1 - y2) / d
    canvas.create_line(x11, y11, x21, y21, tags = "tree")

window = Tk() # Create a window
window.title("Heap Animation") # Set a title

width = 200
height = 200
radius = 20
vGap = 50
canvas = Canvas(window, width = width, height = height)
canvas.pack()

frame1 = Frame(window) # Create and add a frame to window
frame1.pack()

heap = Heap()
Label(frame1, text = "Enter a key").pack(side = LEFT)
key = StringVar()
entry = Entry(frame1, textvariable = key, 
              justify = RIGHT).pack(side = LEFT)
Button(frame1, text = "Insert", command = insert).pack(side = LEFT)
Button(frame1, text = "Delete", command = delete).pack(side = LEFT)

window.mainloop() # Create an event loop
