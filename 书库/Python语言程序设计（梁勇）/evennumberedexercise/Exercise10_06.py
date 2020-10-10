import math

NUM_OF_PRIMES = 50
# Store prime numbers
primeNumbers = []

count = 0 # Count the number of prime numbers
number = 2 # A number to be tested for primeness
isPrime = True # Is the current number prime?

print("The first 50 prime numbers are \n")

# Repeatedly find prime numbers
while ount < NUM_OF_PRIMES:
    # Assume the number is prime
    isPrime = True

    i = 0 
    while i < count and primeNumbers[i] <= math.sqrt(number):
        #If true, the number is not prime
        if number % primeNumbers[i] == 0:
            # Set isPrime to false, if the number is not prime
            isPrime = False
            break # Exit the for loop
        
        i += 1

    # Print the prime number and increase the count
    if isPrime:
        primeNumbers.append(number)
        count += 1 # Increase the count

        if count % 10 == 0:
            # Print the number and advance to the new line
            print(number)
        else:
            print(number, end = " ")

    # Check if the next number is prime
    number += 1
