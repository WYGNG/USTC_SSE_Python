import random

headCount = 0
tailCount = 0

for i in range(100000):
    number = random.randint(0, 1)

    if number == 0:
        headCount += 1
    else:
        tailCount += 1

print("head count:", headCount)
print("tail count:", tailCount)
