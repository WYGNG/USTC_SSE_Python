def format(number, width):
    result = str(number)
    for i in range(0, width - len(number)):
        result = "0" + result
    
    return result
 
def len(number):
    size = 0
    while number > 0:
        size += 1
        number = number // 10
        
    return size    
    
def main():
    number = eval(input("Enter an integer: "))
    width = eval(input("Enter the width: "))
    print("The formatted number is", format(number, width))

main() # Call the main function
