def main():
    count = 1

    i = 2 
    while count <= 100:
        # Display each number in five positions
        if isPrime(i) and isPalindrome(i):
            print(i, end = " ")

            if count % 10 == 0:
                print()

            count += 1 # Increase count
        
        i += 1

def isPrime(number):
    divisor = 2
    while divisor <= number / 2:
        if number % divisor == 0:
            # If true, number is not prime
            return False # number is not a prime
        divisor += 1

    return True # number is prime

# Return the reversal of an integer, i.e. reverse(456) returns 654
def isPalindrome(number):
    return number == reverse(number)

# Return the reversal of an integer, i.e. reverse(456) returns 654
def reverse(number):
    result = 0
    while number != 0:
        remainder = number % 10
        result = result * 10 + remainder
        number = number // 10

    return result

main()
