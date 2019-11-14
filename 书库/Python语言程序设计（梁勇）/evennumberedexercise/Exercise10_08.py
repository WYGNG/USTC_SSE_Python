def main():
    # Read numbers as a string from the console
    s = input("Enter scores separated by spaces from one line: ") 
    items = s.split() # Extracts items from the string
    numbers = [ eval(x) for x in items ] # Convert items to numbers

    print("The index of the smallest element is", indexOfSmallestElement(numbers))
   
def indexOfSmallestElement(list):
    min = list[0]
    minIndex = 0

    for i in range(1, len(list)):
        if min > list[i]:
            min = list[i]
            minIndex = i

    return minIndex

main()
