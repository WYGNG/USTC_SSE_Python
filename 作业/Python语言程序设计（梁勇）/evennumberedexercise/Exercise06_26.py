import time

def main():
    beginTime = time.time()
    
    for p in range(2, 31 + 1):
      i = 2 ** p - 1

      # Display each number in five positions
      if isPrime(i):
          print(p, "\t", i)

    endTime = time.time()
    print("Time spent is", endTime - beginTime, "milliseconds")

def isPrime(number):
    divisor = 2
    while divisor <= number / 2:
        if number % divisor == 0:
            # If true, number is not prime
            return False # number is not a prime
        divisor += 1

    return True # number is prime

# Return the reversal of an integer, i.e. reverse(456) returns 654
def reverse(number):
    result = 0
    while number != 0:
        remainder = number % 10
        result = result * 10 + remainder
        number = number // 10

    return result

main()
