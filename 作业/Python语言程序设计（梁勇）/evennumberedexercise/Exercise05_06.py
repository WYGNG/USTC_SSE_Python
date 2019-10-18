print(format("Miles", "<15s"), format("Kilometers", "10s"), 
      "       |      ", format("Kilometers", "<15s"), format("Miles", "10s"))
print("-----------------------------------------------------------------")

miles = 1
kilometers = 20
count = 1
while count <= 10:
    print(format(miles, "<15d"), format(miles * 1.609, "<10.3f"), "       |      ", 
          format(kilometers, "<15d"), format(kilometers / 1.609, "<10.3f"))
    miles += 1
    kilometers += 5
    count += 1
