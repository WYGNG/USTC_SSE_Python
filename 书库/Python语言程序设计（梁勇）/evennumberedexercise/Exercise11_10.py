import random

n = 4
def main():
    matrix = []
    
    for i in range(n):
        matrix.append([])
        for j in range(n):
            matrix[i].append(random.randint(0, 1))
            print(matrix[i][j], end = " ")

        print()

    # Check rows
    rowSum = sum(matrix[0])
    rowList = [0]
    for i in range(1, n):
        if rowSum < sum(matrix[i]):
            rowSum = sum(matrix[i])
            rowList = [i]
        elif rowSum == sum(matrix[i]):
            rowList.append(i)
            
    print("The largest row index: ", end = "")
    for i in range(len(rowList) - 1):
        print(rowList[i], end = ", ")
    print(rowList[len(rowList) - 1])

    # Check columns
    columnSum = sumColumn(matrix, 0)
    columnList = [0]
    for j in range(1, n):
        if columnSum < sumColumn(matrix, j):
            columnSum = sumColumn(matrix, j)
            columnList = [j]
        elif columnSum == sumColumn(matrix, j):
            columnList.append(j)
            
    print("The largest column index: ", end = "")
    for i in range(len(columnList) - 1):
        print(columnList[i], end = ", ")
    print(columnList[len(columnList) - 1])
    
def sumColumn(m, j):
    sum = 0
    for i in range(n):
        sum += m[i][j]
    return sum

main()
