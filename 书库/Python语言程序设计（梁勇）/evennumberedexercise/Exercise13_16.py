import random

output = open("Salary.txt", "w")

N = 1000
for i in range(N):
    output.write("FirstName" + str(i + 1) + " ")
    output.write("LastName" + str(i + 1) + " ")
    
    rank = random.randint(0, 2)
    if rank == 0:
        output.write("assistant ")
        output.write(str(round(random.random() * 30000 + 50000, 2)))
    elif rank == 1:
        output.write("associate ")
        output.write(str(round(random.random() * 50000 + 60000, 2)))
    else:
        output.write("full ")
        output.write(str(round(random.random() * 55000 + 75000, 2)))

    if  i < N - 1:
        output.write("\n")
