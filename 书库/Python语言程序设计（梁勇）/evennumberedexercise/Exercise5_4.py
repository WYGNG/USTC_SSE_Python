print("{0:<15s}{1:>10s}".format("Miles", "Kilometers"))
print("-----------------------------")

miles = 1
while miles <= 10:
    print("{0:<15d}{1:<10.3f}".format(miles, miles * 1.609))
    miles += 1