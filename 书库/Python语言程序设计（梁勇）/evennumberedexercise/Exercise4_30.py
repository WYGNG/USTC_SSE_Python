import time

# Prompt the user to enter the time zone offset to GMT
timeZoneOffset = eval(input("Enter the time zone offset to GMT: "))

currentTime = time.time() # Get current time

# Obtain the total seconds since midnight, Jan 1, 1970
totalSeconds = int(currentTime)

# Get the current second 
currentSecond = totalSeconds % 60 

# Obtain the total minutes
totalMinutes = totalSeconds // 60 

# Compute the current minute in the hour
currentMinute = totalMinutes % 60

# Obtain the total hours
totalHours = totalMinutes // 60

# Compute the current hour
currentHour = (totalHours + timeZoneOffset) % 24

# Display results
if currentHour < 12:
    print("Current time is " + str(currentHour % 12) + ":"
        + str(currentMinute) + ":" + str(currentSecond) + " AM")
else:
    print("Current time is " + str(currentHour % 12) + ":"
        + str(currentMinute) + ":" + str(currentSecond) + " PM")
      