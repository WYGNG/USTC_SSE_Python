class Stock:
    # Construct a stock object 
    def __init__(self, name, symbol, previousPrice, currentPrice):
        self.__name = name
        self.__symbol = symbol
        self.__previousPrice = previousPrice
        self.__currentPrice = currentPrice

    def getName(self):
        return self.__name 

    def getSymbol(self):
        return self.__symbol

    def getPreviousPrice(self):
        return self.__previousPrice

    def getCurrentPrice(self):
        return self.__currentPrice

    def setPreviousPrice(self, previousPrice):
        self.__previousPrice = previousPrice

    def setCurrentPrice(self, currentPrice):
        self.__currentPrice = currentPrice

    def getHeight(self):
        return self.height

    def getChangePercent(self):
        return format((self.__currentPrice - self.__previousPrice) * 100 / self.__previousPrice, "5.2f") + "%"

def main():
    # Create a rectangle with width 4 and height 40 
    stock = Stock("Intel", "INTC", 20.5, 20.35)
    print("The price change is " + str(stock.getChangePercent()))
          
main()
