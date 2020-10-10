import random
import time

correctCount = 0 # Count the number of correct answers
count = 0 # Count the number of questions
NUMBER_OF_QUESTIONS = 10 # Constant

startTime = time.time() # Get start time

while count < NUMBER_OF_QUESTIONS:
    # 1. Generate two random integers
    number1 = random.randint(1, 15)
    number2 = random.randint(1, 15)

    # 2. If number1 < number2, swap number1 with number2
    if number1 < number2:
        number1, number2 = number2, number1

    # 3. Prompt the student to answer "what is number1 + number2?" 
    answer = eval(input("What is " + str(number1) + " + " + 
        str(number2) + "? "))

    # 4. Grade the answer and display the result
    if number1 + number2 == answer:
        print("You are correct!")
        correctCount += 1
    else:
        print("Your answer is wrong.\n", number1, "+", number2, "should be", 
            number1 + number2)

    # Increase the count
    count += 1

endTime = time.time() # Get end time
testTime = int(endTime - startTime) # Get test time
print("Correct count is", correctCount, "out of", NUMBER_OF_QUESTIONS,
    "\nTest time is", testTime, "seconds\n")
