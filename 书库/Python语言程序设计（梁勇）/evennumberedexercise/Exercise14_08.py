def main():
    # Prompt the user to enter filenames
    f1 = input("Enter a filename: ").strip()

    # Open files for input 
    infile = open(f1, "r")
    
    s = infile.read() # Read all from the file
    infile.close()
    
    words = s.split()
    nonduplicateWords = set(words)
    words = list(nonduplicateWords)
    words.sort()
    
    for word in words:
        print(word, end = " ") 

main()
