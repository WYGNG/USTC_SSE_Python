# Prompt the user to enter the number of students
numOfStudents = eval(input("Enter the number of students: "))

student1 = input("Enter a student name: ")
score1 = eval(input("Enter a student score: "))

for i in range(numOfStudents - 1):
    student = input("Enter a student name: ")
    score = eval(input("Enter a student score: ")) 

    if score > score1:
        student1 = student
        score1 = score

print("Top student " + student1 + "'s score is " + str(score1))
