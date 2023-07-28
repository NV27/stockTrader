import random

# Define classes and functions
class Player:
    def __init__(self, name, startingMoney, money, lemonStock, orangeStock, pineappleStock, starfruitStock):
        self.name = name
        self.startingmoney = startingMoney
        self.money = money
        self.lemonStock = lemonStock
        self.orangeStock = orangeStock
        self.pineappleStock = pineappleStock
        self.starfruitStock = starfruitStock

class Stock:
    def __init__(self, name, startingPrice, price, shelfLife, age):
        self.name = name
        self.startingPrice = startingPrice
        self.price = price
        self.shelfLife = shelfLife
        self.age = age

def getStock(stock):
    print(stock.name + " price is: " + str(stock.startingPrice))

def purchaseStock(var):
    global player
    while True:
        try:
            answer = int(input("\nHow Many " + var.name + "s would you like to buy?\n"))
            max_quantity = int(player.money / var.startingPrice)
            if 1 <= answer <= max_quantity:
                player.money -= answer * var.startingPrice
                setattr(player, var.name.lower() + "Stock", getattr(player, var.name.lower() + "Stock") + answer)
                print("\nYou bought " + str(answer) + " " + var.name + "s, for ¥" + str(answer * var.startingPrice))
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

def priceChange(a):
    a.price = int(a.price + ((random.randint(0,4) - 2) * (a.price/10)))



# Define objects
lemon = Stock("lemon", 50, 50, 7, 0)
orange = Stock("orange", 40, 40, 7, 0)
pineapple = Stock("pineapple", 100, 100, 7, 0)
starfruit = Stock("starfruit", 800, 800, 7, 0)

priceChange(lemon)
priceChange(orange)
priceChange(pineapple)
priceChange(starfruit)

playername = input("What's your name?\n")
player = Player(playername, 200, 200, 0, 0, 0, 0)

# Define other variables
varContinue2 = 1

#Game
print("\nYour name is " 
      + str(player.name) 
      + "\nYou have ¥"
      + str(player.money)
      + "\n\n---SUNDAY---"
      + "\n\nYour objective is to make profit by trading fruit stocks"
      + "\nYou can hold them for 7 days before they go off"
      + "\n\nThese fruit are on the market this week"
      + "\n 1. Lemon: ¥" + str(lemon.price) + " - SL " + str(lemon.shelfLife)
      + "\n 2. Orange: ¥" + str(orange.price) + " - SL " + str(orange.shelfLife)
      + "\n 3. Pineapple: ¥" + str(pineapple.price) + " - SL " + str(pineapple.shelfLife)
      + "\n 4. Starfruit: ¥" + str(starfruit.price) + " - SL " + str(starfruit.shelfLife) 
      )

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

print("\nDaily Stats:")
print("\nYour name is " 
      + str(player.name) 
      + "\nYou have ¥"
      + str(player.money)
      + "\n\nTurnip Stock: " + str(player.lemonStock) + " - ¥" + str(lemon.price) + " each"
      + "\nPotato Stock: " + str(player.orangeStock) + " - ¥" + str(orange.price) + " each"
      + "\nRadish Stock: " + str(player.pineappleStock) + " - ¥" + str(pineapple.price) + " each"
      + "\nGold Radish Stock: " + str(player.starfruitStock) + " - ¥" + str(starfruit.price) + " each"
     )

#DAY 2
