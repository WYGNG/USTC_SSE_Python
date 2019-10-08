# Prompt the user to enter input
year = eval(input("Enter a year: "))
firstDay = eval(input("Enter the first day of the year: "))

numberOfDaysInMonth = 0

# Display calendar for each month
for month in range(1, 12 + 1):
    # Display Calendar title
    if month == 1:
        print("January 1, " + str(year) + " is ", end = "")
        numberOfDaysInMonth = 31
    elif month == 2:
        print("February 1, " + str(year) + " is ", end = "")
        if (year % 400 == 0 or (year % 4 == 0 and year % 100 != 0)):
            numberOfDaysInMonth = 29
        else:
            numberOfDaysInMonth = 28
    elif month == 3:
        print("March 1, " + str(year) + " is ", end = "")
        numberOfDaysInMonth = 31
    elif month == 4:
        print("April 1, " + str(year) + " is ", end = "")
        numberOfDaysInMonth = 30
    elif month == 5:
        print("May 1, " + str(year) + " is ", end = "")
        numberOfDaysInMonth = 31
    elif month == 6:
        print("June 1, " + str(year) + " is ", end = "")
        numberOfDaysInMonth = 30
    elif month == 7:
        print("July 1, " + str(year) + " is ", end = "")
        numberOfDaysInMonth = 31
    elif month == 8:
        print("August 1, " + str(year) + " is ", end = "")
        numberOfDaysInMonth = 31
    elif month == 9:
        print("September 1, " + str(year) + " is ", end = "")
        numberOfDaysInMonth = 30
    elif month == 10:
        print("October 1, " + str(year) + " is ", end = "")
        numberOfDaysInMonth = 31
    elif month == 11:
        print("November 1, " + str(year) + " is ", end = "")
        numberOfDaysInMonth = 30
    elif (month == 12):
        print("December 1, " + str(year) + " is ", end = "")
        numberOfDaysInMonth = 31

    if firstDay == 0:
        print("Sunday") 
    elif firstDay == 1:
        print("Monday") 
    elif firstDay == 2:
        print("Tuesday") 
    elif firstDay == 3:
        print("Wednesday") 
    elif firstDay == 4:
        print("Thursday") 
    elif firstDay == 5:
        print("Friday") 
    elif firstDay == 6:
        print("Saturday") 

    # Get the start day for the next month
    firstDay = (firstDay + numberOfDaysInMonth) % 7