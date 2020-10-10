import os

def main():
    # Prompt the user to enter a directory or a file
    path = input("Enter a directory or a file: ").strip()  
   
    # Display the size
    try:
        print("The number of files is " + str(getNumberOfFiles(path)))
    except:
        print("File or directory does not exist")

def getNumberOfFiles(path):
    size = 0 # Store the total number of files

    if not os.path.isfile(path):
        list = os.listdir(path) # All files and subdirectories
        for i in range(len(list)):
            size += getNumberOfFiles(path + "\\" + list[i]) 
    else: # Base case, it is a file
        size += 1 # os.path.getsize(path) # Accumulate file count

    return size

main()
