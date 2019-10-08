def main():
    # Read numbers as a string from the console
    s = input("Enter numbers separated by spaces from one line: ") 
    items = s.split() # Extracts items from the string
    numbers = [ eval(x) for x in items ] # Convert items to numbers
    print("The largest number in " + str(numbers) + " is " + str(largest(numbers)))
    
def largest(list):
    return largestHelper(list, len(list) - 1)

def largestHelper(list, high):
    if high == 0:
        return list[0]
    else:
      return max(largestHelper(list, high - 1), list[high])

main()
