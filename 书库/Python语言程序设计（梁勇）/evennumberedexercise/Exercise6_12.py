def main():
    printChars('1', 'Z', 10)

def printChars(ch1, ch2, numberPerLine):
    count = 1
      
    for i in range(ord(ch1), ord(ch2) + 1):
        if count % numberPerLine == 0:
            print(chr(i))        
        else:
            print(chr(i), end = "")
            
        count += 1

main()