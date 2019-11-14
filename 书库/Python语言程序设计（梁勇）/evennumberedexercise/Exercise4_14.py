import random

# Obtain the random number 0 or 1
number = random.randint(0, 1)

# Prompt the user to enter a guess
guess = eval(input("Guess head or tail? " + \
      "Enter 0 for head and 1 for tail: "))
print(number)
# Check the guess
if guess == number:
    print("Correct guess")
elif number == 0:
    print("Sorry, it is a head")
else:
    print("Sorry, it is a tail")