# Prompt the user to enter weight in pounds
weight = eval(input("Enter weight in pounds: "))
    
# Prompt the user to enter height 
feet = eval(input("Enter feet: "))
inches = eval(input("Enter inches: "))

height = feet * 12 + inches
    
# Compute BMI
bmi = weight * 0.45359237 / ((height * 0.0254) * (height * 0.0254))
    
# Display result
print("BMI is", bmi)
if bmi < 18.5:
    print("Underweight")
elif bmi < 25:
    print("Normal")
elif bmi < 30:
    print("Overweight")
else:
    print("Obese")
