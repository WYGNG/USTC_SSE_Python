def main():
    status = eval(input("(0-single filer, 1-married jointly,\n" +
            "2-married separately, 3-head of household)\n" +
            "Enter the filing status: "))

    # Prompt the user to enter taxable income
    income = eval(input("Enter the taxable income: "))

    # Compute and display the result
    print("Tax is", format(computeTax(status, income), "7.2f"))

def computeTax(status, income):
    rates = [0.10, 0.15, 0.25, 0.28, 0.33, 0.35]
        
    brackets = [
      [8350, 33950, 82250, 171550, 372950],   # Single filer
      [16700, 67900, 137050, 20885, 372950], # Married jointly
      [8350, 33950, 68525, 104425, 186475], # Married separately
      [11950, 45500, 117450, 190200, 372950] # Head of household
    ]

    tax = 0 # Tax to be computed

    # Compute tax in the first bracket
    if income <= brackets[status][0]:
        return income * rates[0] # Done
    else:
        tax = brackets[status][0] * rates[0]

        # Compute tax in the 2nd, 3rd, 4th, and 5th brackets, if needed
        for i in range(1, len(brackets[0])):
            if income > brackets[status][i]:
                tax += (brackets[status][i] - brackets[status][i - 1]) * rates[i]
            else:
                tax += (income - brackets[status][i - 1]) * rates[i]
                return tax # Done

            # Compute tax in the last (i.e., 6th) bracket
            return  tax + (income - brackets[status][4]) * rates[5]

main()
