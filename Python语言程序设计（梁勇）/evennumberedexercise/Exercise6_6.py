def main():
    lineNumber = eval(input("Enter line number: "))
    displayPattern(lineNumber);

def displayPattern(n):
    for row in range(1, n + 1):
        # Print spaces
        for i in range(row, n):
            print("  ", end = "")

        # Print numbers
        for i in range(row, 0, -1):
            print(" " + str(i), end = "")

        print()
        
main()