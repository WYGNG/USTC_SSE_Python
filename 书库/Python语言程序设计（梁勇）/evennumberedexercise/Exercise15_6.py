def fib(index):
    global count
    count += 1

    if index == 0: # Base case
        return 0
    elif index == 1: # Base case
        return 1
    else:  # Reduction and recursive calls
        return fib(index - 1) + fib(index - 2)

index = eval(input("Enter an index for the Fibonacci number: "))
count = 0
fib(index)
print("Number of times fib invoked is " + str(count))