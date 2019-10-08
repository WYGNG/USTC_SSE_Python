import time

class Time:
    def __init__(self):
        self.setTime(int(time.time()))

    def getHour(self):
        return self.__hour

    def getMinute(self):
        return self.__minute

    def getSecond(self):
        return self.__second
    
    def setTime(self, elapsedTime):
        # Get the current second 
        self.__second = elapsedTime % 60
        
        # Obtain the total minutes
        totalMinutes = elapsedTime // 60 
        
        # Compute the current minute in the hour
        self.__minute = totalMinutes % 60
        
        # Obtain the total hours
        totalHours = totalMinutes // 60
        
        # Compute the current hour
        self.__hour = totalHours % 24
    
def main():
    currentTime = Time()
    print("Current time is " + str(currentTime.getHour()) + ":" + str(currentTime.getMinute()) + ":" + str(currentTime.getSecond()))

    elapseTime = eval(input("Enter the elapse time: "))
    currentTime.setTime(elapseTime)
    print("The hour:minute:second for elapse time is " + str(currentTime.getHour()) + ":" + str(currentTime.getMinute()) + ":" + str(currentTime.getSecond()))

main()
