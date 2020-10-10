def main():
    s = input("Enter characters separated by spaces from one line: ").strip()
    items = s.split() # Extracts items from the string
    ch = input("Enter a character: ").strip()
    print("The number of occurrence of character " + ch + " in " + str(items) + " is " + str(count(items, ch)))
    
def count(chars, ch):
    return countHelper(chars, ch, len(chars) - 1)

def countHelper(chars, ch, high):
    if high >= 0:
        return countHelper(chars, ch, high - 1) + (1 if chars[high] == ch else 0)
    else:
        return 0
    
main()
