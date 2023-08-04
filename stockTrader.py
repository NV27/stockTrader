import random

# Define classes and functions
class Player:
    def __init__(self, name, startingMoney, money, lemonStock, orangeStock, pineappleStock, starfruitStock, income):
        self.name = name
        self.startingmoney = startingMoney
        self.money = money
        self.lemonStock = lemonStock
        self.orangeStock = orangeStock
        self.pineappleStock = pineappleStock
        self.starfruitStock = starfruitStock
        self.income = income

class Stock:
    def __init__(self, name, startingPrice, price, shelfLife, age, sellPercent, fruitYield):
        self.name = name
        self.startingPrice = startingPrice
        self.price = price
        self.shelfLife = shelfLife
        self.age = age
        self.sellPercent = sellPercent
        self.fruitYield = fruitYield

def getStock(stock):
    print(stock.name + " price is: " + str(stock.startingPrice))

def whatToDo():
    while True:
        try:
            answer = int(input("\nWhat would you like to do\n 1.buy\n 2.sell\n 3.continue to next day\n"))
            if answer == 1:
                break
            if answer == 2:
                #Which Stock?
                while True:
                    try:
                        answer = int(input("What would you like to sell?\n"))
                        if 1 <= answer <= 4:
                            break
                        else:
                            print("Please enter a valid number (1-4)")
                    except ValueError:
                        print("Please enter a number")

                if answer == 1:
                    var = lemon

                if answer == 2:
                    var = orange

                if answer == 3:
                    var = pineapple

                if answer == 4:
                    var = starfruit
                sellStock(var)
            if answer == 3:
                global varContinue2
                varContinue2 = 0
                break
            else:
                print("Please enter a number between 1 and 2")
        except ValueError:
            print("Please enter a number")

def purchaseStock(var):
    global player
    while True:
        try:
            answer = int(input("\nHow Many " + var.name + "s (¥" + str(var.price) + ") would you like to buy?\n"))
            print( "\n\nLemon: ¥" + str(lemon.price)
            + "\nOrange: ¥" + str(orange.price)
            + "\nPineapple: ¥" + str(pineapple.price)
            + "\nStarfruit: ¥" + str(starfruit.price))
            max_quantity = int(player.money / var.price)
            if 1 <= answer <= max_quantity:
                player.money -= answer * var.price
                setattr(player, var.name.lower() + "Stock", getattr(player, var.name.lower() + "Stock") + answer)
                print("\nYou bought " + str(answer) + " " + var.name + "s, for ¥" + str(answer * var.price))
                print("You have ¥" + str(player.money) + " remaining")
                varContinue = input("\n1. Buy more " + var.name + "s \n2. Continue\n")
                if varContinue.lower() != "1":
                    break
            else:
                if answer != 0:
                    print("You can't buy that many")
                else:
                    break
        except ValueError:
            print("Please enter a number")


def sellStock(var):
    global player
    while True:
        try:
            varStock = getattr(player, var.name.lower() + "Stock")
            answer = int(input("\nYou have " + str(varStock) + " " + var.name + "s\nHow Many " + var.name + "s would you like to sell?\n"))
            max_quantity = int(varStock)
            if 1 <= answer <= varStock:
                player.money += round(answer * var.price * var.sellPercent)
                varStock -= answer
                setattr(player, var.name.lower() + "Stock", getattr(player, var.name.lower() + "Stock") - answer)
                print("\nYou sold " + str(answer) + " " + var.name + "s, for ¥" + str(round(answer * var.price * var.sellPercent)))
                print("You now have ¥" + str(player.money) + " and " + str(varStock) + " " + str(var.name.lower()) + "s")
                varContinue = input("\n1. Sell more " + var.name + "s \n2. Continue\n")
                if varContinue.lower() != "1":

                    break
            else:
                if answer != 0:
                    print("You don't have that many to sell!")
                else:
                    break
        except ValueError:
            print("Please enter a number")


def priceChange(a):
    a.price = int(a.price + ((random.randint(0,4) - 2) * (a.price/10)))
    
    #if a.name == lemon:

    #if a.name == orange:

    #if a.name == pineapple:

    #if a.name == starfruit:
    

def dailyIntro():
    priceChange(lemon)
    priceChange(orange)
    priceChange(pineapple)
    priceChange(starfruit)

    print("\nYour name is " 
        + str(player.name) 
        + "\n\n--- DAY " + str(day) + " ---"
        + "\n\nYour objective is to make profit by trading fruit stocks"
        + "\nYou have a daily income of ¥20 plus a percentage value of any fruit you currently hold"
        + "\nFruit has a 10% tax on sale"
        + "\n\nYou made ¥" + str(stockYield) + " from the fruit you hold!"
        + "\nYou have ¥"
        + str(player.money)
        + "\n\nNo. NAME  |  PRICE|HOLD|YIELD"
        + "\n 1. Lemon:     ¥" + str(lemon.price) + "  (" + str(player.lemonStock) + ") [" + str(int(lemon.fruitYield*100)) + "%]"
        + "\n 2. Orange:    ¥" + str(orange.price) + "  (" + str(player.orangeStock) + ") [" + str(int(orange.fruitYield*100)) + "%]"
        + "\n 3. Pineapple: ¥" + str(pineapple.price) + " (" + str(player.pineappleStock) + ") [" + str(int(pineapple.fruitYield*100)) + "%]"
        + "\n 4. Starfruit: ¥" + str(starfruit.price) + " (" + str(player.starfruitStock) + ") [" + str(int(starfruit.fruitYield*100)) + "%]"
        )

def dailyStats():
    print("\nDaily Stats:")
    print("\nYour name is " 
      + str(player.name) 
      + "\nYou have ¥"
      + str(player.money)
      + "\n\nLemon Stock: " + str(player.lemonStock) + " - ¥" + str(lemon.price) + " each"
      + "\nOrange Stock: " + str(player.orangeStock) + " - ¥" + str(orange.price) + " each"
      + "\nPineapple Stock: " + str(player.pineappleStock) + " - ¥" + str(pineapple.price) + " each"
      + "\nStarfruit Stock: " + str(player.starfruitStock) + " - ¥" + str(starfruit.price) + " each"
     )
    
def calcStockYield():
    global stockYield
    stockYield = int((player.lemonStock * lemon.fruitYield * lemon.price)
    + (player.orangeStock * orange.fruitYield * orange.price)
    + (player.pineappleStock * pineapple.fruitYield * pineapple.price)
    + (player.starfruitStock * starfruit.fruitYield * starfruit.price))



# Define objects and variables
lemon = Stock("lemon", 50, 50, 7, 0, 0.9, 0.1)
orange = Stock("orange", 40, 40, 7, 0, 0.9, 0.1)
pineapple = Stock("pineapple", 200, 200, 7, 0, 0.9, 0.12)
starfruit = Stock("starfruit", 800, 800, 7, 0, 0.9, 0.2)

playername = input("What's your name?\n")
player = Player(playername, 200, 200, 0, 0, 0, 0, 20)
global varContinue2
varContinue2 = 1
global stockYield
stockYield = 0

# Define other variables
day = 1
playing = 1


while playing:
    #Game
    varContinue2 = 1
    dailyIntro()

###
    whatToDo()
###

    while varContinue2 == 1:
        #Which Stock?
        while True:
            try:
                answer = int(input("What would you like to buy?\n"))
                if 1 <= answer <= 4:
                    break
                else:
                    print("Please enter a valid number (1-4)")
            except ValueError:
                print("Please enter a number")

        if answer == 1:
            var = lemon

        if answer == 2:
            var = orange

        if answer == 3:
            var = pineapple

        if answer == 4:
            var = starfruit

        #How many?
        purchaseStock(var)

        varContinue2 = int(input("\n\n1.Buy something else\n2.Continue\n"))

    dailyStats()
    calcStockYield()
    day += 1
    player.money += int(player.income + stockYield)

#DAY 2
