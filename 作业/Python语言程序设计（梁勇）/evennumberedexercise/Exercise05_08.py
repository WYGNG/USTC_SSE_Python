import math

print(format("RealNumber", "<15s"), format("SquareRoot", "<15s"))
print("-------------------------------")

for num in range(20 + 1):
    print(format(num, "<15d"), format(math.sqrt(num), "<15.4f"))
