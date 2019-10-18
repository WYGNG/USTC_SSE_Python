rate= eval(input("Enter the exchange rate from dollars to RMB: "))
conversionType = eval(input("Enter 0 to convert dollars to RMB and 1 vice versa: "))

if conversionType == 0:
    dollars =  eval(input("Enter the dollar amount: "))
    RMB = dollars * rate
    print(format(dollars, ".2f"), "dollars is", format(RMB, ".2f"), "Yuan")
elif conversionType == 1:
    RMB = eval(input("Enter the RMB amount: "))
    dollars = RMB / rate
    print(format(RMB, ".2f"), "Yuan is", format(dollars, ".2f"), "dollars")
else:
    print("Incorrect input")
