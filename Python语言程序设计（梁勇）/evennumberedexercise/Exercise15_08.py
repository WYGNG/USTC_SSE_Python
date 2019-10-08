def main():
    i = eval(input("Enter an integer: "))
    reverseDisplay(i)

def reverseDisplay(value):
    if value != 0:
        print(value % 10, end = "")
        value = value // 10
        reverseDisplay(value)

main()
