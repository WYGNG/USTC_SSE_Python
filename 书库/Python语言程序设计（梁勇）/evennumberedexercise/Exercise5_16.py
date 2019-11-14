# Enter n1
n1 = eval(input("Enter the first number: "))

# Enter n2
n2 = eval(input("Enter the second number: "))

d = n1 if n1 < n2 else n2
while d >= 1:
    if n1 % d == 0 and n2 % d == 0:
        break
    d -= 1

print("GCD of", n1, "and", n2, "is", d)