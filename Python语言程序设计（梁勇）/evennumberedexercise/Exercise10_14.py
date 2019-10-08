import random

def main():
    # Read numbers as a string from the console
    s = input("Enter numbers: ") 
    items = s.split() # Extracts items from the string
    numbers = [ eval(x) for x in items ] # Convert items to numbers
    selectionSort(numbers)
    print(numbers)

# The function for sorting the numbers 
def selectionSort(list):
    for i in range(len(list) - 1, 0, -1):
        # Find the minimum in the list[i..len(list)-1]
        currentMax = list[i]
        currentMaxIndex = i

        for j in range(i):
            if currentMax < list[j]:
                currentMax = list[j]
                currentMaxIndex = j

        # Swap list[i] with list[currentMinIndex] if necessary;
        if currentMaxIndex != i:
            list[currentMaxIndex] = list[i]
            list[i] = currentMax

main()
