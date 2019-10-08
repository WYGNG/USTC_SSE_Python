import turtle
from random import shuffle

def drawHistogram(list):
    for i in range(len(list)):     
        draw(list, i)
    
def draw(list, i):
    height = list[i] * HEIGHT / max(list) 
    drawABar(-WIDTH / 2 + i * widthOfBar + 10, 
        -HEIGHT / 2, widthOfBar - 5, height)     
    drawAString(-WIDTH / 2 + i * widthOfBar + 18, 
        -HEIGHT / 2 + height + 10, str(list[i]))   

def drawABar(i, j, widthOfBar, height):
    turtle.penup()
    turtle.goto(i, j)
    turtle.setheading(90) # Set orientation to north
    turtle.pendown()

    turtle.forward(height) # Draw a vertical line
    turtle.right(90) # Turn right 90 degrees
    turtle.forward(widthOfBar) # Draw a horizontal line
    turtle.right(90) # Turn right 90 degrees
    turtle.forward(height) # Draw a vertical line

def drawAString(i, j, ch):
    turtle.penup()
    turtle.goto(i, j)
    turtle.setheading(90) # Set orientation to north
    turtle.pendown()
    turtle.write(ch) 
    
def swap(list, i, j):       
    turtle.color("white")
    draw(list, j)
    draw(list, i)
    
    list[i], list[j] = list[j], list[i]
    turtle.color("black")
    draw(list, j)
    draw(list, i)
    
# The function for sorting the numbers 
def selectionSort(list):
    for i in range(len(list) -1):
        # Find the minimum in the list[i..len(list)-1]
        currentMin = list[i]
        currentMinIndex = i

        for j in range(i + 1, len(list)):
            if currentMin > list[j]:
                currentMin = list[j]
                currentMinIndex = j

        # Swap list[i] with list[currentMinIndex] if necessary;
        if currentMinIndex != i:
           # list[currentMinIndex] = list[i]
           # list[i] = currentMin
           swap(list, i, currentMinIndex)    
        
list1 = list(range(1, 21)) # Create a list with elements 3, 4, 5
shuffle(list1)  
  
turtle.hideturtle()      
WIDTH = 600 # Width of the histogram
HEIGHT = 300 # Height of the histogram

# Draw a base line
turtle.penup()
turtle.goto(-WIDTH / 2, -HEIGHT / 2)
turtle.pendown()
turtle.forward(WIDTH)

widthOfBar = WIDTH / len(list1) # Width of each bar

turtle.speed(0) # fast
drawHistogram(list1)

turtle.speed(1) # slow

selectionSort(list1)

turtle.done()