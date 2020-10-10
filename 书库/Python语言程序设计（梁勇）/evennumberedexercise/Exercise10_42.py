def main():
    s = input("Enter a string: ").strip()
    print("The sorted string is " + sort(s))

def sort(s):
    r = list(s)
    r.sort()
    
    result = ""
    for ch in r:
        result += ch
        
    return result

main()
