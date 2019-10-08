def main():
    s = input("Enter a string: ").strip()
    ch = input("Enter a character: ").strip()

    print(count(s, ch))

def count(s, ch):
    count = 0
    for c in s:
        if ch == c:
            count += 1
            
    return count
  
main()