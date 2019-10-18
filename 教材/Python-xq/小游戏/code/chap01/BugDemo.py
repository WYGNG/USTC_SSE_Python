# OOP Bug Demo

class Bug(object):
    legs = 0
    distance = 0

    def __init__(self, name="Bug", legs=6):
        self.name = name
        self.legs = legs

    def Walk(self,distance=1):
        self.distance += distance

    def GetDistance(self):
       return distance

    def SetDistance(self, value):
        distance = value

    def ToString(self):
        return self.name + " has " + str(self.legs) + " legs" + \
            " and taken " + str(self.distance) + " steps."
        

#default constructor
ant = Bug()
for n in range(0,5):
    ant.Walk()
print(ant.ToString())

#one constructor parameter
beetle = Bug("Beetle")
beetle.legs = 6
for n in range(0,10):
    beetle.Walk()
print(beetle.ToString())

#two constructor parameters
spider = Bug("Spider", 8)
for n in range(0,10):
    spider.Walk(2)
print(spider.ToString())

