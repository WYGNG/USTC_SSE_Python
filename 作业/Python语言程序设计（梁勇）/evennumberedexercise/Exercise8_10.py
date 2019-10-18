def main():
    value = eval(input("Enter an integer: "))
    print("The binary value is " + str(decimalToBinary(value)))

def decimalToBinary(value):
    result = ""

    while value != 0:
        bit = value % 2;
        result = str(bit) + result
        value = value // 2

    return result

main()