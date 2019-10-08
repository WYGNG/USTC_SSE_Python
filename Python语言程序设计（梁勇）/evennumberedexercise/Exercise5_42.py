import random

NUMBER_OF_TRIALS = 1000000
numberOfHits = 0

for i in range(NUMBER_OF_TRIALS):
    x = random.random() * 2.0 - 1;
    y = random.random() * 2.0 - 1;
    if x < 0:
        numberOfHits += 1
    elif not (x > 1 or x < 0 or y > 1 or y < 0):
        slope = (1.0 - 0) / (0 - 1.0)
        x1 = x + -y * slope
        if x1 <= 1:
          numberOfHits += 1

print("The probability in Region 1 and 3 is " +
      str(1.0 * numberOfHits / NUMBER_OF_TRIALS))