# Input number of years
numberOfYears = eval(input("Enter the number of years: "))

# Compute population
population = 312032486 + numberOfYears * 365 * 24 * 60 * 60 // 7 - \
    numberOfYears * 365 * 24 * 60 * 60 // 13 + numberOfYears * 365 * 24 * 60 * 60 // 45;
    
# Display results
print("The population in", numberOfYears, "years is", population)