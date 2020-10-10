def main():
    # Read numbers as a string from the console
    s = input("Enter numbers: ") 
    items = s.split() # Extracts items from the string
    numbers = [ eval(x) for x in items ] # Convert items to numbers
    reverse(numbers)
    print(numbers)

def reverse(list):
    for i in range(len(list) // 2):
        list[i], list[len(list) -i -1] =  list[len(list) -i -1], list[i] 

    return list
        
main()
