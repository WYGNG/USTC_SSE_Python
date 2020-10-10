def main():
    f1 = input("Enter a source filename: ").strip()
    f2 = input("Enter a target filename: ").strip()

    # Open files for input 
    infile = open(f1, "r")
    
    s = infile.read() # Read all from the file
    
    newS = ""
    
    for i in range(len(s)):
        newS += chr(ord(s[i]) + 5)

    infile.close()  # Close the input file
    outfile = open(f1, "w")
    
    print(newS, file = outfile, end = "") # Write to the file
    print("Done") 

    outfile.close() # Close the output file

main()
