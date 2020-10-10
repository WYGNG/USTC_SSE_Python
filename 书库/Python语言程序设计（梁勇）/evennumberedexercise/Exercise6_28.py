import random
import sys

def main():
    dice = getDice()
    if dice == 7 or dice == 11:
        print("You win")
        sys.exit()
    elif dice == 2 or dice == 3 or dice == 12:
        print("You lose")
        sys.exit()

    point = dice
    print("point is", point)
    
    dice = getDice()
    while dice != 7 and dice != point:
        dice = getDice()
    
    if dice == 7:
        print("You lose")
    else:
        print("You win")

# Get a dice
def getDice():
    i1 = random.randint(1, 6)
    i2 = random.randint(1, 6)

    print("You rolled", i1, "+", i2, "=", i1 + i2)
    return i1 + i2

main()