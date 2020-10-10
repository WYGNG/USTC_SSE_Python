def main():
    # Declare, create, and initialized array
    workHours = [
        [2, 4, 3, 4, 5, 8, 8],
        [7, 3, 4, 3, 3, 4, 4],
        [3, 3, 4, 3, 3, 2, 2],
        [9, 3, 4, 7, 3, 4, 1],
        [3, 5, 4, 3, 6, 3, 8],
        [3, 4, 4, 6, 3, 4, 4],
        [3, 7, 4, 8, 3, 8, 4],
        [6, 3, 5, 9, 2, 7, 9]]

    # Create an array to store total weekly hours
    weeklyHours = []
    for i in range(len(workHours)):
        weeklyHours.append([sum(workHours[i]), i])
        
    weeklyHours.sort()
    
    # Display result
    for empolyeeHours in weeklyHours:
        print("Employee " + str(empolyeeHours[1]) + ": " + str(empolyeeHours[0]))

main()
