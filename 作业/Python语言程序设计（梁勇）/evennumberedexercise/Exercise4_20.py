import sys

# Enter the temperature in Fahrenheit
fahrenheit = eval(input("Enter the temperature in Fahrenheit: ")) 

if fahrenheit < -58 or fahrenheit > 41:
    print("Temperature must be between -58F and 41F")
    sys.exit()

# Enter the wind speed miles per hour
speed = eval(input("Enter the wind speed miles per hour: "))
    
if speed < 2:
    print("Speed must be greater than or equal to 2")
    sys.exit()

# Compute wind chill index
windChillIndex = 35.74 + 0.6215 * fahrenheit - 35.75 * \
      speed ** 0.16 + 0.4275 * fahrenheit * speed ** 0.16
      
# Display the result
print("The wind chill index is " + str(windChillIndex))