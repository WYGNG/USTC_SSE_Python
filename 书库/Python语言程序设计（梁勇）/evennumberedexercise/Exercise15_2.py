def main():   
    m = eval(input("Enter the first number: "))
    n = eval(input("Enter the first number: "))

    print("The GCD of " + str(m) + " and " + str(n) + " is " + str(gcd(m, n)))

def gcd(m, n):
    if m % n == 0:
        return n
    else:
        return gcd(n, m % n)

main()