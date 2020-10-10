import math

class QuadraticEquation:
    def __init__(self, a, b, c):
        self.__a = a
        self.__b = b
        self.__c = c

    def getA(self):
        return self.__a

    def getB(self):
        return self.__b
    
    def getC(self):
        return self.__c
    
    def getDiscriminant(self):
        return self.__b * self.__b - 4 * self.__a * self.__c

    def getRoot1(self):
        if self.getDiscriminant() < 0:
            return 0
        else:
            return (-self.__b + self.getDiscriminant()) / (2 * self.__a)

    def getRoot2(self):
        if self.getDiscriminant() < 0:
            return 0
        else:
            return (-self.__b - self.getDiscriminant()) / (2 * self.__a)

def main():
    a, b, c = eval(input("Enter a, b, c: "))
    equation = QuadraticEquation(a, b, c)
    discriminant = equation.getDiscriminant()

    if discriminant < 0:
        print("The equation has no roots")
    elif discriminant == 0:
        print("The root is " + str(equation.getRoot1()))
    else: # (discriminant >= 0)
        print("The roots are " + str(equation.getRoot1()) + " and " + str(equation.getRoot2())) 
          
main()