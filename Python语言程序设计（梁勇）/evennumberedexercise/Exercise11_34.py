def main():
    line = input("Enter six points: ").split()
    p = [[eval(line[i]), eval(line[i + 1])] for i in range(0, 6, 2)]
    
    point = getRightmostLowestPoint(p)
    
    print("The rightmost lowest point is (" + 
      str(point[0]) + ", " + str(point[1]) + ")")
  
def getRightmostLowestPoint(p):
    rightMostIndex = 0
    rightMostX = p[0][0]
    rightMostY = p[0][1]
    
    for i in range(1, len(p)):
        if rightMostY > p[i][1]:
            rightMostY = p[i][1]
            rightMostIndex = i
        elif rightMostY == p[i][1] and rightMostX < p[i][0]:
            rightMostX = p[i][0]
            rightMostIndex = i
  
    return [p[rightMostIndex][0], p[rightMostIndex][1]]

main()
