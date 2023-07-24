import random

# Define classes and functions
class Player:
    def __init__(self, name, startingMoney, money, turnipStock, potatoStock, radishStock, goldRadishStock):
        self.name = name
        self.startingmoney = startingMoney
        self.money = money
        self.turnipStock = turnipStock
        self.potatoStock = potatoStock
        self.radishStock = radishStock
        self.goldRadishStock = goldRadishStock

class Stock:
    def __init__(self, name, startingPrice):
        self.name = name
        self.startingPrice = startingPrice

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
                print("You can't buy that many")
        except ValueError:
            print("Please enter a number")



# Define objects
turnip = Stock("turnip", 5)
potato = Stock("potato", 3)
radish = Stock("radish", 10)
goldRadish = Stock("gold radish", 80)

playername = input("What's your name?\n")
player = Player(playername, 20, 20, 0, 0, 0, 0)

# Define other variables
varContinue2 = 1

#Game
print("\nYour name is " 
      + str(player.name) 
      + "\nYou have ¥"
      + str(player.money)
      + "\n\n---SUNDAY---"
      + "\n\nYour objeective is to make profit by trading vegetable stocks"
      + "\nYou can hold them for 7 days before they go off"
      + "\n\nThese vegetables are on the market this week"
      + "\n 1. Turnip: ¥5"
      + "\n 2. Potato: ¥3"
      + "\n 3. Radish: ¥10"
      + "\n 4. Golden Raddish: ¥80"
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
        var = turnip

    if answer == 2:
        var = potato

    if answer == 3:
        var = radish

    if answer == 4:
        var = goldRadish

    #How many?
    purchaseStock(var)

    varContinue2 = int(input("\n\n1.Buy something else\n2.Continue\n"))

print("\nThanks for playing! Final details:")
print("\nYour name is " 
      + str(player.name) 
      + "\nYou have ¥"
      + str(player.money)
      + "\nTurnip Stock: " + str(player.turnipStock)
      + "\nPotato Stock: " + str(player.potatoStock)
      + "\nRadish Stock: " + str(player.radishStock)
      + "\nGold Radish Stock: " + str(player.goldRadishStock)
      + "\n\nGoodbye!"
     )

'''
while True:
    if answer <= 4:
        try:
            answer = int(input("\nHow Many?\n"))
            if 1 <= answer <= (player.money/var.startingPrice):
                var2 = answer
                player.money -= answer*var.startingPrice
                print("\nYou bought " + str(var2) + " turnips, for ¥" + str(answer*var.startingPrice))
                print("You have ¥" + str(player.money) + " remaining")
                break
            else:
                print("You can't afford that many")
                break
        except ValueError:
            print("Pleae enter a number")
'''


'''
while True:
    if answer == 1:
        try:
            answer = int(input("Buy something else? \n"))
            if 1 <= answer <= (player.money/turnip.startingPrice):
                player.turnipStock = answer
                player.money -= answer*turnip.startingPrice
                break
            else:
                print("Please enter a number")
        except ValueError:
            print("You can't afford that many")
'''