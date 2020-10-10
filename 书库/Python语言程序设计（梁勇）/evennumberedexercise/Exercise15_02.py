def main():
    index = eval(input("Enter an index for Fibonacci number: "))  
    print("The Fibonacci number at index " + str(index) + " is " + str(fib(index)))

def fib(n):
    f0 = 0
    f1 = 1
   
    if n == 0: 
        return 0
    if n == 1: 
        return 1

    for i in range(2, n + 1):
        currentFib = f0 + f1
        f0 = f1
        f1 = currentFib

    return f1

main()
