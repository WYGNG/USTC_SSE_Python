import random

count = 0

while count <= 2 or count <= -2:
    # Generate scissor, rock, paper
    computerNumber = random.randint(0, 2)

    # Prompt the user to enter scissor, rock, or paper
    userNumber = eval(input("scissor (0), rock (1), paper (2): "))

    # Check the guess
    if computerNumber == 0:
        if userNumber == 0:
            print("It is a draw")
        elif userNumber == 1: 
            print("You won")
            count += 1       
        elif userNumber == 2:
            print("You lost")
            count -= 1
    elif computerNumber == 1:
        if userNumber == 0:
            print("You lost")
            count -= 1
        elif userNumber == 1:
            print("It is a draw")
        elif userNumber == 2:
            print("You won")
            count += 1
    elif computerNumber == 2:
        if userNumber == 0:
            print("You won")
            count += 1       
        elif userNumber == 1:
            print("You lost")
            count -= 1
        elif userNumber == 2: 
            print("It is a draw")

if count > 2: 
    print("You won more than two times")
else:
    print("The computer won more than two times")

