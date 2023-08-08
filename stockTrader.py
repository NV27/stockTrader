import random

# Define classes and functions
class Player:
    def __init__(self, name, startingMoney, money, lemonStock, orangeStock, pineappleStock, starfruitStock, income, rent, rentPrev):
        self.name = name
        self.startingmoney = startingMoney
        self.money = money
        self.lemonStock = lemonStock
        self.orangeStock = orangeStock
        self.pineappleStock = pineappleStock
        self.starfruitStock = starfruitStock
        self.income = income
        self.rent = rent
        self.rentPrev = rentPrev

class Stock:
    def __init__(self, name, startingPrice, price, shelfLife, age, sellPercent, fruitYield, patternFunction):
        self.name = name
        self.startingPrice = startingPrice
        self.price = price
        self.shelfLife = shelfLife
        self.age = age
        self.sellPercent = sellPercent
        self.fruitYield = fruitYield
        self.patternFunction = patternFunction

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


def priceChange(stock):
    stock.patternFunction(stock)

def patternA(stock):
    stock.price = int(stock.price + ((random.randint(0,4) - 2) * (stock.price/10)))

def patternB(stock):
    stock.price -= int(round((stock.price * random.randrange(0,3,1) * 0.01)))

def patternC(stock):
    stock.price += int(round((stock.price * random.randrange(0,3,1) * 0.01)))

def patternD(stock):
    stock.price += int(round(19 * random.randrange(0,3,1)))

def patternE(stock):
    if day % 7 != 4:
        stock.price -= int(round((stock.price * random.randrange(0,3,1) * 0.01)))
    else:
        stock.price *= 2

def patternF(stock):
    if day % 7 == 4:
        stock.price *= 2
    if day % 7 == 6:
        stock.price *= 2
    else:
        stock.price -= int(round((stock.price * random.randrange(0,3,1) * 0.02)))
    

def dailyIntro():
    priceChange(lemon)
    priceChange(orange)
    priceChange(pineapple)
    priceChange(starfruit)

    weekDay = weekDayArray[day%7]

    print("\nYour name is " 
        + str(player.name)
        + "\n\n--- Day " + str(day) + " - " + str(weekDay) +" ---"
        + "\n\nYour objective is to make profit by trading fruit stocks"
        + "\nFruit follows a different price pattern each week"
        + "\n\nYou make a daily income based on the value of any fruit you currently hold"
        + "\nYour rent is currently $" + str(player.rent) + "/week, which you pay on Sundays"
        + "\nFruit has a 10% tax on sale"
        + "\n\nYou made ¥" + str(stockYield) + " from the fruit you hold!"
        )
    if day%7==0:
        print("RENT DAY - You payed $" + str(player.rentPrev))
    print("You have ¥"
        + str(player.money)
        + "\n\nNo. NAME  |  PRICE|HOLD|YIELD"
        + "\n 1. Lemon:     ¥" + str(lemon.price) + "  (" + str(player.lemonStock) + ") [" + str(int(lemon.fruitYield*100)) + "%] " #+ str(lemon.patternFunction)
        + "\n 2. Orange:    ¥" + str(orange.price) + "  (" + str(player.orangeStock) + ") [" + str(int(orange.fruitYield*100)) + "%] " #+ str(orange.patternFunction)
        + "\n 3. Pineapple: ¥" + str(pineapple.price) + " (" + str(player.pineappleStock) + ") [" + str(int(pineapple.fruitYield*100)) + "%] " #+ str(pineapple.patternFunction)
        + "\n 4. Starfruit: ¥" + str(starfruit.price) + " (" + str(player.starfruitStock) + ") [" + str(int(starfruit.fruitYield*100)) + "%] " #+ str(starfruit.patternFunction)
        )
    player.rentPrev = player.rent

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
patternArray = [patternA,patternB,patternC,patternD,patternE,patternF]
PAlength = len(patternArray)
weekDayArray = ["Sunday", "Monday", "Tuesday", "Wednesday", "Thursdsay", "Friday", "Saturday"]

lemon = Stock("lemon", 50, 50, 7, 0, 0.9, 0.1, patternArray[random.randint(0,PAlength-1)])
orange = Stock("orange", 40, 40, 7, 0, 0.9, 0.1, patternArray[random.randint(0,PAlength-1)])
pineapple = Stock("pineapple", 200, 200, 7, 0, 0.9, 0.12, patternArray[random.randint(0,PAlength-1)])
starfruit = Stock("starfruit", 800, 800, 7, 0, 0.9, 0.2, patternArray[random.randint(0,PAlength-1)])

playername = input("What's your name?\n")
player = Player(playername, 200, 200, 0, 0, 0, 0, 20, 100, 100)
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
    if day % 7 == 0:
        lemon.patternFunction = patternArray[random.randint(0,2)]
        orange.patternFunction = patternArray[random.randint(0,2)]
        pineapple.patternFunction = patternArray[random.randint(0,2)]
        starfruit.patternFunction = patternArray[random.randint(0,2)]
        #print("NEW PATTERNS")
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
    #player.money += int(player.income + stockYield)
    player.money += int(stockYield)
    if day%7==0:
        player.money -= player.rent
        player.rent += int(round(player.rent/5))

    if player.money < 0:
        print("\nAs Saturday night ticks over to Sunday"
              + "\nYou feel your weekly rent magically ripped from your pocket"
              + "\nWith it comes your soul"
              + "\nYou are Broke"
              + "\nYou are Dead"
              + "\nThanks for playing!"
              +"\n\nYOU SURVIVED FOR " + str(day) + " DAYS\n"
              )
        playing = 0
