import time

def main():
    # Find the first 45 Fibonacci numbers
    INDEX = 47
    numbers = INDEX * [0]
    numbers[0] = 0
    numbers[1] = 1
    for i in range(2, INDEX):
        numbers[i] = numbers[i - 1] + numbers[i - 2]

    print("\t\t\t40\t41\t42\t43\t44\t45")
    print("-------------------------------------------------------------");
    print("Listing 16.2 GCD1")

    executionTime = 6 * [0]

    for i in range(40, 45 + 1):
        startTime = time.time()
        gcd1(numbers[i], numbers[i + 1])
        executionTime[i - 40] = time.time() - startTime

    for i in range(5 + 1):
        print("\t" + str(executionTime[i]))

    print("\nListing 16.3 GCD2");

    for i in range(40, 45 + 1):
        startTime = System.currentTimeMillis()
        gcd2(numbers[i], numbers[i + 1])
        executionTime[i - 40] = time.time() - startTime

    for i in range(0, 5 + 1):
        print("\t" + str(executionTime[i]))

# Find gcd for integers m and n 
def gcd1(m, n):
    gcd = 1
    
    if m % n == 0:
        return n
    
    for k in range(int(n / 2), 0, -1):
        if m % k == 0 and n % k == 0:
            gcd = k
            break
    
    return gcd

# Find gcd for integers m and n 
def gcd2(m, n):
    if m % n == 0:
        return n
    else:
        return gcd(n, m % n)
    
main()