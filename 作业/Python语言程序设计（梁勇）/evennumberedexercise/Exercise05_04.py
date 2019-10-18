print(format("Miles", "<15s"), format("Kilometers", ">10s"))
print("--------------------------------")

miles = 1
while miles <= 10:
    print(format(miles, "<15d"), format(miles * 1.609, "<10.3f"))
    miles += 1
