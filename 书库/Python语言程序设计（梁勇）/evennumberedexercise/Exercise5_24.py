# Enter loan amount
loanAmount = eval(input("Enter loan amount, for example 120000.95: "))

# Enter number of years
numOfYears = eval(input("Enter number of years as an integer, for example 5: "))

# Enter yearly interest rate
annualInterestRate = eval(input("Enter yearly interest rate, for example 8.25: "))

# Obtain monthly interest rate
monthlyInterestRate = annualInterestRate/1200

# Compute mortgage
monthlyPayment = loanAmount*monthlyInterestRate / \
    (1 - (pow(1 / (1 + monthlyInterestRate), numOfYears * 12)))

balance = loanAmount
print("Monthly Payment: " + str(int(monthlyPayment * 100) / 100.0))
print("Total Payment: " + str(int(monthlyPayment * 12 * numOfYears * 100) / 100.0))

# Display the header
print("Payment#\tInterest\tPrincipal\tBalance")
for i in range(1, numOfYears * 12 + 1):
    interest = int(monthlyInterestRate * balance * 100) / 100.0
    principal = int((monthlyPayment - interest) * 100) / 100.0
    balance = int((balance - principal) * 100) / 100.0
    print(str(i) + "\t\t" + str(interest) + "\t\t" + str(principal) + "\t\t" + str(balance))