def main():
    print("{0:<15s}{1:<15s} |    {2:<15s}{3:<15s}".format("Celsius", "Fahrenheit", "Fahrenhei", "Celsius")) 
    print("-----------------------------------------------------------")

    celsius = 40
    farenheit = 120
    i = 1
    
    while i <= 10:
        print("{0:<15d}{1:<15.2f} |    {2:<15d}{3:<15.2f}".format(celsius, celsiusToFahrenheit(celsius), farenheit, fahrenheitToCelsius(farenheit)))
        celsius -= 1
        farenheit -= 10
        i += 1

# Converts from Celsius to Fahrenheit 
def celsiusToFahrenheit(celsius):
    return (9.0 / 5.0) * celsius + 32

# Converts from Fahrenheit to Celsius 
def fahrenheitToCelsius(fahrenheit):
    return (5.0 / 9) * (fahrenheit - 32)

main()