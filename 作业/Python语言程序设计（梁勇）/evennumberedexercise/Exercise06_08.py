def main():
    print(format("Celsius", "<15s"), format("Fahrenheit", "<15s"), "  |    ", format("Fahrenhei", "<15s"), format("Celsius", "<15s")) 
    print("---------------------------------------------------------------")

    celsius = 40
    farenheit = 120
    i = 1
    
    while i <= 10:
        print(format(celsius, "<15d"), format(celsiusToFahrenheit(celsius), "<15.2f"), "  |    ", 
              format(farenheit, "<15d"), format(fahrenheitToCelsius(farenheit), "<15.2f"))
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
