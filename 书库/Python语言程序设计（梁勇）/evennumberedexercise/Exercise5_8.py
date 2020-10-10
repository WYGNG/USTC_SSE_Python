import math

print("{0:<15s}{1:<15s}".format("RealNumber", "SquareRoot"))
print("-------------------------------")

for num in range(20 + 1):
    print("{0:<15d}{1:<15.4f}".format(num, math.sqrt(num)))