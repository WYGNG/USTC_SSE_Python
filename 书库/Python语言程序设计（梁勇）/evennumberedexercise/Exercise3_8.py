# Receive the amount 
amount = eval(input("Enter an amount as integer, e.g., 1156 for 11 dollars 56 cents: "))

# Convert the amount to cents
remainingAmount = amount

# Find the number of one dollars
numberOfOneDollars = remainingAmount // 100
remainingAmount = remainingAmount % 100

# Find the number of quarters in the remaining amount
numberOfQuarters = remainingAmount // 25
remainingAmount = remainingAmount % 25

# Find the number of dimes in the remaining amount
numberOfDimes = remainingAmount // 10
remainingAmount = remainingAmount % 10

# Find the number of nickels in the remaining amount
numberOfNickels = remainingAmount // 5
remainingAmount = remainingAmount % 5

# Find the number of pennies in the remaining amount
numberOfPennies = remainingAmount

# Display results
print("Your amount " + str(amount) + " consists of \n" + 
      "\t" + str(numberOfOneDollars) + " dollars\n" + 
      "\t" + str(numberOfQuarters) + " quarters\n" +
      "\t" + str(numberOfDimes) +  " dimes\n" + 
      "\t" + str(numberOfNickels) + " nickels\n" +
      "\t" + str(numberOfPennies) + " pennies")