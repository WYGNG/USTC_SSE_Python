def main():
    # Read numbers as a string from the console
    s = input("Enter numbers: ") 
    items = s.split() # Extracts items from the string
    numbers = [ eval(x) for x in items ] # Convert items to numbers
    if ordered(numbers):
        print("The numbers in the list are in ascending order")
    else:
        print("The numbers in the list are not in ascending order")
        
def ordered(list, ord = "ascending"):
    if ord == "ascending":
        for i in range(len(list) - 1):
          if list[i] >= list[i + 1]:
            return False
    
        return True
    else:
        for i in range(len(list) - 1):
          if list[i] <= list[i + 1]:
            return False
    
        return True

main()
