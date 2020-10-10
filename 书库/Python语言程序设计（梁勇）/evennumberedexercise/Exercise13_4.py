from random import randint
import os.path

def main():
    # Prompt the user to enter filenames
    f1 = input("Enter a filename: ").strip()

    if os.path.isfile(f1):
        print("The file already exists")
        return
    
    # Open files for output 
    outfile = open(f1, "w")
    
    for i in range(100):
        print(randint(0, 999), file = outfile, end = " ")
    
    outfile.close()
    
    infile = open(f1, "r")
    s = infile.read() # Read all from the file

    numbers = [eval(items) for items in s.split()]
    numbers.sort()
    
    for i in range(len(numbers)):
        print(numbers[i], end = " ")
        
    infile.close() # Close the output file

main()
