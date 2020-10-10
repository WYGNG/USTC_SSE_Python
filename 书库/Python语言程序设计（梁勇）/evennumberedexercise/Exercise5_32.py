monthlyDeposit = eval(input("Enter the amount to be saved for each month: "))
    
annualInterestRate = eval(input("Enter the annual interest rate: "))
monthlyInterestRate = annualInterestRate / 1200

numberOfMonths = eval(input("Enter the number of months: "))

currentValue = monthlyDeposit * (1 + monthlyInterestRate)
for i in range(1, numberOfMonths):
    currentValue = (currentValue + monthlyDeposit) * (1 + monthlyInterestRate)

print("After the " + str(numberOfMonths) + "th month, the account value is " + str(currentValue))
