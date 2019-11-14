def main():
    decimal = eval(input("Enter a decimal integer: "))
    print(str(decimal) + " is binary " + decimalToHex(decimal))

def decimalToHex(value):
    if value == 0:
      return ""
    else:
      if value % 16 == 10:
        temp = "A"
      elif value % 16 == 11:
        temp = "B"
      elif value % 16 == 12:
        temp = "C"
      elif value % 16 == 13:
        temp = "D"
      elif value % 16 == 14:
        temp = "E"
      elif (value % 16 == 15):
        temp = "F"
      else:
        temp = str(value % 16)
  
      return decimalToHex(value // 16) + temp

main()
