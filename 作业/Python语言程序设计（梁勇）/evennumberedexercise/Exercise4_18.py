rate= eval(input("Enter the exchange rate from dollars to RMB: "))
conversionType = eval(input("Enter 0 to convert dollars to RMB and 1 vice versa: "))

if conversionType == 0:
    dollars =  eval(input("Enter the dollar amount: "))
    RMB = dollars * rate
    print("${0:.2f} is {1:.2f} Yuan".format(dollars, RMB))
elif conversionType == 1:
    RMB = eval(input("Enter the RMB amount: "))
    dollars = RMB / rate
    print("{0:.2f} Yuan is ${1:.2f}".format(RMB, dollars))
else:
    print("Incorrect input")