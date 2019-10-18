def main():
    matrix1 = []
    matrix2 = []
    
    s = input("Enter a 3-by-3 matrix1: ") 
    items = s.split() # Extracts items from the string
    for i in range(3):
        list = [eval(items[j]) for j in range(3 * i, 3 * i + 3)] # Convert items to numbers   
        matrix1.append(list)

    s = input("Enter a 3-by-3 matrix2: ") 
    items = s.split() # Extracts items from the string
    for i in range(3):
        list = [eval(items[j]) for j in range(3 * i, 3 * i + 3)] # Convert items to numbers   
        matrix2.append(list)
        
    matrix3 = multiplyMatrix(matrix1, matrix2)
    printResult(matrix1, matrix2, matrix3, "*")
    
def multiplyMatrix(m1, m2):
    list = len(m2[0]) * [0]
    result = []  
    for i in range(len(m1)):
        result.append([x for x in list])
    
    for i in range(len(result)):
        for j in range(len(result[0])):
            for k in range(len(m2)):
                result[i][j] += m1[i][k] * m2[k][j]
        
    return result
          
# Print result 
def printResult(m1, m2, m3, op):
    for i in range(len(m1)):
        for j in range(len(m1[0])):
            print(" " + str(m1[i][j]), end = "")

        if i == len(m1) // 2:
            print( "  " + op + "  ", end = "")
        else:
            print( "     ", end = "")

        for j in range(len(m2[0])):
            print(" " + str(m2[i][j]), end = "")

        if i == len(m1) // 2:
            print("  =  ", end = "")
        else:
            print("     ", end = "")

        for j in range(len(m3[0])):
            print(" " + str(m3[i][j]), end = "")

        print()
        
main()
