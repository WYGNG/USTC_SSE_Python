SLOW = 1
MEDIUM = 2
FAST = 3

class Fan:
    def __init__(self, speed = SLOW, radius = 5, color = "blue", on = False):
        self.__speed = speed
        self.__radius = radius
        self.__color = color
        self.__on = on

    def getSpeed(self):
        return self.__speed

    def getRadius(self):
        return self.__radius

    def getColor(self):
        return self.__color

    def isOn(self):
        return self.__on

    def setSpeed(self, speed):
        self.__speed = speed

    def setRadius(self, radius):
        self.__radius = radius

    def setColor(self, color):
        self.__color = color

    def setOn(self, on):
        self.__on = on

def displayProperties(fan):
    print("speed", fan.getSpeed(), "\n", "color", fan.getColor(), "\n", 
        "radius", fan.getRadius(), "\n", "fan is on" if fan.isOn() else "fan is off")

def main():
    fan1 = Fan()
    fan1.setSpeed(FAST)
    fan1.setRadius(10)
    fan1.setColor("yellow")
    fan1.setOn(True)
    displayProperties(fan1)

    fan2 = Fan()
    fan2.setSpeed(MEDIUM)
    fan2.setRadius(5)
    fan2.setColor("blue")
    fan2.setOn(False)
    displayProperties(fan2)
          
main()