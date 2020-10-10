number = eval(input("Enter a three-digit integer: "))

reversedNumber = (number % 10) * 100 + (number // 10 % 10) * 10 + (number // 100)

if number == reversedNumber:
    print(number, "is a palindrome")
else:
    print(number, "is not a palindrome")