def main():
    for year in range(2000, 2010 + 1):
        print(str(year) + " has " + str(numberOfDaysInAYear(year)))

def numberOfDaysInAYear(year):
    if isLeapYear(year):
      return 366
    else:
      return 365


# Determine if it is a leap year *
def isLeapYear(year):
    return year % 400 == 0 or (year % 4 == 0 and year % 100 != 0)

main()