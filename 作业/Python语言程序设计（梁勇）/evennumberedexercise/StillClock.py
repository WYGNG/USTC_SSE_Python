from tkinter import * # Import tkinter
import math 
from datetime import datetime
   
class StillClock(Canvas):
    def __init__(self, container, width = 100, height = 110):
        Canvas.__init__(self, container, width = width, height = height)
        self.setCurrentTime()
    
    def getHour(self):
        return self.hour
    
    def setHour(self, hour):
        self.hour = hour
        self.delete("clock")
        self.drawClock()
        
    def getMinute(self):
        return self.minute

    def setMinute(self, minute):
        self.minute = minute
        self.delete("clock")
        self.drawClock()

    def getSecond(self):
        return self.second

    def setSecond(self, second):
        self.second = second
        self.delete("clock")
        self.drawClock()

    def setCurrentTime(self):
        d = datetime.now()
        self.hour = d.hour
        self.minute = d.minute
        self.second = d.second
        self.delete("clock")
        self.drawClock()    
        
    def drawClock(self):        
        width = float(self["width"])
        height = float(self["height"])
        radius = min(width, height) / 2.4
        secondHandLength = radius * 0.8
        minuteHandLength = radius * 0.65
        hourHandLength = radius * 0.5
        
        self.create_oval(width / 2 - radius, height / 2 - radius, 
            width / 2 + radius, height / 2 + radius, tags = "clock")
        self.create_text(width / 2 - radius + 5, height / 2, 
                         text = "9", tags = "clock")
        self.create_text(width / 2 + radius - 5, height / 2, 
                         text = "3", tags = "clock")
        self.create_text(width / 2, height / 2 - radius + 5, 
                         text = "12", tags = "clock")
        self.create_text(width / 2, height / 2 + radius - 5, 
                         text = "6", tags = "clock")
                
        xCenter = width / 2
        yCenter = height / 2
        second = self.second
        xSecond = xCenter + secondHandLength \
            * math.sin(second * (2 * math.pi / 60))
        ySecond = yCenter - secondHandLength \
            * math.cos(second * (2 * math.pi / 60))
        self.create_line(xCenter, yCenter, xSecond, ySecond, 
                         fill = "red", tags = "clock")
        
        minute = self.minute
        xMinute = xCenter + \
            minuteHandLength * math.sin(minute * (2 * math.pi / 60))
        yMinute = yCenter - \
            minuteHandLength * math.cos(minute * (2 * math.pi / 60))
        self.create_line(xCenter, yCenter, xMinute, yMinute, 
                         fill = "blue", tags = "clock")
        
        hour = self.hour % 12
        xHour = xCenter + hourHandLength * \
            math.sin((hour + minute / 60) * (2 * math.pi / 12))
        yHour = yCenter - hourHandLength * \
            math.cos((hour + minute / 60) * (2 * math.pi / 12))
        self.create_line(xCenter, yCenter, xHour, yHour, 
                         fill = "green", tags = "clock")
        
        timestr = str(hour) + ":" + str(minute) + ":" + str(second)
        self.create_text(width / 2, height / 2 + radius + 10, 
                         text = timestr, tags = "clock")
