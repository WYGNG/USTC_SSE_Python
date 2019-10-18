# Obtain input
balance, annualInterestRate = eval(input("Enter balance and annual interest rate: "))

monthlyInterestRate = annualInterestRate / 1200;

interest = balance * monthlyInterestRate;

# Display output
print("The interest is", (int)(100* interest) / 100.0)