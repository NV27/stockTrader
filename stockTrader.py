import random

# Define classes and functions
class Player:
    def __init__(self, name, startingMoney, money, turnipStock, potatoStock, raddishStock, goldRaddishStock):
        self.name = name
        self.startingmoney = startingMoney
        self.money = money
        self.turnipStock = turnipStock
        self.potatoStock = potatoStock
        self.raddishStock = raddishStock
        self.goldRaddishStock = goldRaddishStock

class Stock:
    def __init__(self, name, startingPrice):
        self.name = name
        self.startingPrice = startingPrice

def getStock(stock):
    print(stock.name + " price is: " + str(stock.startingPrice))

#Lodef buyStock(stock):

# Define objects

turnip = Stock("turnip", 5)
potato = Stock("potato", 3)
raddish = Stock("raddish", 10)
goldRaddish = Stock("gold raddish", 80)

playername = input("What's your name?\n")
player = Player(playername, 20, 20, 0, 0, 0, 0)

#Game
print("\nYour name is " 
      + str(player.name) 
      + "\nYou have "
      + str(player.money)
      + " dollars"
      + "\n\n Your objeective is to make profit by trading vegetable stocks"
      + "\n You can hold them for 7 days before they go off"
      + "\n What would you like to buy?"
      + "\n 1. Turnip: ¥5"
      + "\n 2. Potato: ¥3"
      + "\n 3. Raddish: ¥10"
      + "\n 4. Golden Raddish: ¥80"
      )

#Which Stock?
while True:
    try:
        answer = int(input("What would you like to buy?\n"))
        if 1 <= answer <= 4:
            break
        else:
            print("Please enter a number")
    except ValueError:
        print("Please enter a valid number")

#How many?
while True:
    if answer == 1:
        try:
            answer = int(input("\nHow Many?\n"))
            if 1 <= answer <= (player.money/turnip.startingPrice):
                player.turnipStock = answer
                player.money -= answer*turnip.startingPrice
                break
            else:
                print("Please enter a number")
        except ValueError:
            print("You can't afford that many")

print("\nYou bought " + str(player.turnipStock) + " turnips, for ¥" + str(answer*turnip.startingPrice))
print("You have ¥" + str(player.money) + " remaining")
input("Buy something else? \n")