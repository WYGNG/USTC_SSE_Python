NUMBER_OF_CARDS = 52
    
import random

# Pick a card
number = random.randint(0, NUMBER_OF_CARDS - 1)

print("The card you picked is", end = " ")
if number % 13 == 0:
    print("Ace of ", end = "")
elif number % 13 == 10:
    print("Jack of ", end = "")
elif number % 13 == 11:
    print("Queen of ", end = "")
elif number % 13 == 12:
    print("King of ", end = "")
else:
    print(number % 13, "of ", end = "")

if number // 13 == 0:
    print("Clubs")
elif number // 13 == 1:
    print("Diamonds")
elif number // 13 == 2:
    println("Hearts")
elif number // 13 == 3:
    print("Spades")