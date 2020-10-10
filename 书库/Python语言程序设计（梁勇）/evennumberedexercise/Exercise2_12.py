# Enter the investment amount
finalAccountValue = eval(input("Enter final account value: "))

# Enter yearly interest rate
annualInterestRate = eval(input("Enter annual interest rate in percent, for example 8.25: "))

# Obtain monthly interest rate
monthlyInterestRate = annualInterestRate / 1200

# Enter number of years
numOfYears = eval(input("Enter number of years as an integer, \nfor example 5: "))

initialDepositValue = finalAccountValue / (1 + monthlyInterestRate) ** (numOfYears * 12)

print("Initial deposit value is", initialDepositValue)
