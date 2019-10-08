print("{0:<15s}{1:10s}       |      {0:<15s}{1:10s}".format("Miles", "Kilometers", "Kilometers", "Miles" ))
print("------------------------------------------------------------")

miles = 1
kilometers = 20
count = 1
while count <= 10:
    print("{0:<15d}{1:<10.3f}       |      {2:<15d}{3:<10.3f}".format(miles, miles * 1.609, kilometers, kilometers / 1.609))
    miles += 1
    kilometers += 5
    count += 1