def main():
    SIZE = 3
    print("Enter a 3 by 3 matrix row by row: ")
    m = []
    
    for i in range(SIZE):
        line = input().split()
        m.append([eval(x) for x in line])

    print("The row-sorted list is ")
    printMatrix(sortRows(m))

def printMatrix(m):
    for i in range(len(m)):
        for j in range(len(m[i])):
            print(m[i][j], end = " ")
        print()
        
def sortRows(m):
    result = []
    for row in m:
         result.append(row)
    
    for row in result:
        row.sort()

    return result

main()
