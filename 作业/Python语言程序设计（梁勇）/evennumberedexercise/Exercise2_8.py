# Prompt the user to enter a degree in Celsius
mass = eval(input("Enter the amount of water in kilograms: "))

initialTemperature = eval(input("Enter the initial temperature: "))
    
finalTemperature = eval(input("Enter the final temperature: "))

energy =  mass * (finalTemperature - initialTemperature) * 4184

print("The energy needed is " + str(energy))