def main():
    first = input("Enter the first string: ").strip()
    second = input("Enter the second string: ").strip()
   
    if isSubstring(first, second) != -1: 
        print(first + " is a substring of " + second)
    else:
        print(first + " is not a substring of " + second)
        
# Check if the first string is a substring of the second string
def isSubstring(first, second):
    remainingLength = len(second)
    startingIndex = 0;

    while len(first) <= remainingLength:
        if first != second[startingIndex : startingIndex + len(first)]:
            startingIndex += 1
            remainingLength -= 1
        else:
            return startingIndex 

    return -1

main()