def main():
    s = input("Enter a string: ").strip()

    print("The number of letters in", s, "is", count(s))
   
def count(s):
    result = 0
    for c in s:
        if c.isalpha():
            result += 1
            
    return result
  
main()
