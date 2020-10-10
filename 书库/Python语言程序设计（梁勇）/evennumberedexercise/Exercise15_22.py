def main():
    hex = input("Enter a hex number: ").strip()
    print(hex + " is decimal " + str(hexToDecimal(hex)))

def hexToDecimal(hexString):
    return hexToDecimalHelper(hexString, 0, len(hexString) - 1)
  
def hexToDecimalHelper(hexString, low, high):
    if high < low:
        return 0
    else:
        if hexString[high] == 'A':
            temp = 10
        elif hexString[high] == 'B':
            temp = 11
        elif hexString[high] == 'C':
            temp = 12
        elif hexString[high] == 'D':
            temp = 13
        elif hexString[high] == 'E':
            temp = 14
        elif hexString[high] == 'F':
            temp = 15
        else:
            temp = ord(hexString[high]) - ord('0')

        return hexToDecimalHelper(hexString, low, high - 1) * 16 + temp

main()
