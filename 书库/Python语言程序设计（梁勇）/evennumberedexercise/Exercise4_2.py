import random 

# Generate random numbers
number1 = random.randint(0, 9)
number2 = random.randint(0, 9)
number3 = random.randint(0, 9)

# Prompt the user to enter an answer
answer = eval(input("What is " + str(number1) + " + " 
    + str(number2) + " + " + str(number3) + "? "))
    
# Display result    
print(number1, "+", number2, "+", number3, "=", answer,
    "is", (number1 + number2 + number3 == answer))