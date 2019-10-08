def main():
    s = input("Enter a string: ").strip()
    ch = input("Enter a character: ")[0]
    times = count(s, ch)
    print(ch + " appears " + str(times) + (" times " if times > 1 else " time ") + "in " + s)
    
def count(s, a):
    return countHelper(s, a, len(s) - 1)

def countHelper(s, a, high):
    result = 0;
    if high >= 0:
        result = countHelper(s, a, high - 1) + (1 if s[high] == a else 0)

    return result;

main()
