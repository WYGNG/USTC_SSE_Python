from Rational import Rational

sum = Rational(0, 1)

for i in range(1, 10):
    sum = sum + Rational(i, i + 1)
    
# Display results
print("Sum is " + str(sum))
