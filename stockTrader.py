import random

# Define classes and functions
#class Player:
#    def __init__(self):


class Stock:
    def __init__(self, name, startingPrice):
        self.name = name
        self.startingPrice = 0

def getStock():
    print(str(Stock.name) + "Price is: " + Stock.startingPrice)

# Define objects
turnip = Stock("turnip", 5)
potato = Stock("potato", 3)



#Game
getStock()