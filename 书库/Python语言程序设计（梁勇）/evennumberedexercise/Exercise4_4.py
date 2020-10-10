import random 

# Generate random numbers
number1 = random.randint(0, 99)
number2 = random.randint(0, 99)

# Prompt the user to enter an answer
answer = eval(input("What is " + str(number1) + " + " 
    + str(number2) + "? "))
    
# Display result    
print(number1, "+", number2, "=", answer, "is", (number1 + number2 == answer))
