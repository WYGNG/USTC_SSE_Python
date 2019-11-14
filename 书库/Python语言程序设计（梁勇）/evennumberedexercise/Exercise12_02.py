class Location:
    def __init__(self, row, column, maxValue):
        self.row = row
        self.column = column
        self.maxValue = maxValue

    def getRow(self):
        return self.row
    
    def getColumn(self):
        return self.column

    def getMaxValue(self):
        return self.maxValue
    
def main():
    row, column = eval(input("Enter the number of rows and columns of the list: "))
    
    matrix = []
    for i in range(row):
        s = input("Enter row " + str(i) + ": ") 
        items = s.split() # Extracts items from the string
        list = [ eval(x) for x in items ] # Convert items to numbers   
        matrix.append(list)
    
    location = locateLargest(matrix)
    print("The location of the largest element is "
      + str(location.getMaxValue()) + " at (" 
      + str(location.getRow()) + ", " + str(location.getColumn()) + ")")

def locateLargest(a):
    maxValue = a[0][0]
    row = 0
    column = 0
    for i in range(len(a)):
        for j in range(len(a[i])):
            if maxValue < a[i][j]:
                maxValue = a[i][j]
                row = i
                column = j
        
    return Location(row, column, maxValue)

main()
