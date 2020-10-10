def main():
    count = 0
    N = 10000
    for number in range(2, N):
        if isPrime(number):
            count += 1

    print("The number of prime number < " + str(10000) + " is " + str(count))

# Check whether number is prime 
def isPrime(number):
    for divisor in range(2, number // 2 + 1):
        if number % divisor == 0: # If true, number is not prime
            return False # number is not a prime

    return True # number is prime

main()