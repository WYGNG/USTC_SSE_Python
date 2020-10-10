import math

COUNT = 10 # Total numbers
sum = 0 # Store the sum of the numbers
squareSum = 0 # Store the sum of the squares

# Create numbers, find its sum, and its square sum
for i in range(COUNT):
     # Get a new number
     number = eval(input("Enter a number: "))

     # Add the number to sum
     sum += number

     # Add the square of the number to squareSum
     squareSum += number ** 2 # Same as number*number

# Find mean
mean = sum / COUNT

# Find standard deviation
deviation = math.sqrt((squareSum - sum * sum / COUNT) / (COUNT - 1))

# Display result
print("The mean is " + str(mean))
print("The standard deviation is " + str(deviation))
