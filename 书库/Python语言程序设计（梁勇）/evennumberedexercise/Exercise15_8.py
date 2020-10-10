def main():
    s = input("Enter a string: ").strip()
    reverseDisplay(s);

def reverseDisplay(value):
    if len(value) > 0:
        print(value[len(value) - 1], end = "")
        reverseDisplay(value[0 : len(value) - 1])

main()