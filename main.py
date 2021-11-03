import random
import json
import time
import os
haslooted = False
firstTime = True
food1 = ""
food2 = ""
weaponForSale = ""
r = ""
doors = 0
useable = ""
previous = True
inv = ["\nmedicine"]


class character:
    def __init__(self, currentHealth, maxHealth, money, hunger, thirst):
        self.cHealth = currentHealth
        self.mHealth = maxHealth
        self.money = money
        self.hunger = hunger
        self.thirst = thirst
    def giveHealth(self):
        print(f"Your current health is {self.cHealth} and your max health is {self.mHealth}\nYour hunger is {self.hunger} and your thirst is {self.thirst}\nYou have £{self.money}")
    def damageTook(self, damage):
        self.cHealth -= damage
        if self.cHealth == 0 or self.cHealth < 0:
            print("Game over! you died")
        else:
            print(f"You lost {damage} health, and now have {self.cHealth} left")



class weapon:
    def __init__(self, durability):
        self.durability = durability




knifeWeapon = weapon(150)
forkWeapon = weapon(40)
batWeapon = weapon(60)










player = character(100,100,50,100,100)
class regularenemy:
  def __init__(self, health, strength):
    self.health = health
    self.strength = strength








def use(item, encounter):
    MaxHealthItems = ["medicine"]
    CurrentHealthItems = ["bandage"]
    weapons = ["knife", "fork", "bat", "torch", "crowbar", "branch", "shovel"]
    hungerItems = ["waterbottle", "carrot", "tomato", "chocolate", "cannedfood", "steak"]
    thirstItems = ["tomato", "carrot", "waterbottle", "chocolate", "cannedfood", "steak"]

    with open ("stats.json", "r") as f:
        data = json.load(f)

        if item in weapons:
            print("You cant use a weapon when there is no enemies to use it on")
            if encounter == "enemy":
                encounterChoice()

            elif encounter == "trader":
                traderchoice()
            else:
                choices()




        elif item in hungerItems and item in thirstItems:
            findThirst = data["thirst"]
            findHunger = data["hunger"]
            randomHunger = random.choice(findHunger[item])
            randomThirst = random.choice(findThirst[item])

            hungerDifference = 100 - player.hunger
            thirstDifference = 100 - player.thirst

            if randomThirst > thirstDifference or randomHunger > hungerDifference:
                player.thirst += thirstDifference
                player.hunger += hungerDifference

            else:
                player.hunger += randomHunger
                player.thirst += randomThirst
            print(f"you used {item} and gained {randomHunger} hunger and {randomThirst} thirst")
            print(f"your current hunger and thirst levels are {player.hunger} and {player.thirst}")
            inv.remove(item)

            if encounter == "enemy":
                encounterChoice()

            elif encounter == "trader":
                traderchoice()
            else:
                choices()




        elif item in MaxHealthItems:
            FindOption = data["maxhealth"]
            ToAdd = random.choice(FindOption[item])
            player.mHealth += ToAdd
            inv.remove("\n"+item)
            print(f"Max health increased to {player.mHealth}")
            if encounter == "enemy":
                encounterChoice()

            elif encounter == "trader":
                traderchoice()
            else:
                choices()

        elif item in CurrentHealthItems:
            FindOption2 = data["currenthealth"]

            ToAdd2 = random.choice(FindOption2[item])





            difference = player.mHealth - player.cHealth

            if ToAdd2 > difference:
                player.cHealth += difference

                print(f"current health increased to {player.cHealth}")

            else:
                player.cHealth += ToAdd2
                print(f"current health increased to {player.cHealth}")

            inv.remove("\n" + item)
            if encounter == "enemy":
                encounterChoice()

            elif encounter == "trader":
                traderchoice()
            else:
                choices()

def startchoice():
    choice = input("> ")
    if choice.lower() == "help":
        print("help - shows this menu")
        print("loot - look around your room for anything useful")
        print("1 - goes through door 1 ")
        print("2 - goes through door 2 (If you have 2 doors available) ")
        print("3 - goes through door 2 (If you have 3 doors available) ")
        startchoice()
    elif choice.lower() == "play":
        os.system("clear")
        generation(r)

def startscreen():
    print("Type 'help' for a list of commands or 'play' to start")
    startchoice()







# "Create" current room
def room():

    global haslooted
    global doors
    global r
    with open("rooms.json") as f:
        haslooted = False
        data = json.load(f)
        r = random.choice(data["rooms"])
        doors = (random.randint(1,3))




def loot(r):
    global haslooted
    global doors


    if doors == 1:
        lucky = random.randint(1,101)


    elif doors == 2:
        lucky = random.randint(1,76)

    elif doors == 3:
        lucky = random.randint(1,51)

    spots = ["You peaked in a cupboard", "You looked in a draw", "You opened a cabinet"]
    gathered = (random.choice(r["LootTables"]))


    if haslooted == False:
        if lucky < 33:
            haslooted = True
            print(f"{random.choice(spots)} and found {gathered}!")

            inv.append(f"\n{gathered}")
            choices()

        else:
            haslooted = True
            print("Looks like you didn't find anything, unlucky")
            choices()
    else:
        print("You have already looted this room!")
        choices()






# room()
# generation(r)



def choices():
    global useable
    global doors
    choice = input("> ")

    if choice.lower() == "loot":
        loot(r)


    elif choice.lower() == "help":
        print("help - shows this menu")
        print("loot - look around your room for anything useful")
        print("1 - goes through door 1 ")
        print("2 - goes through door 2 (If you have 2 doors available) ")
        print("3 - goes through door 2 (If you have 3 doors available) ")
        choices()


    elif choice.lower() == "1":
        os.system("clear")
        room()
        generation(r)


    elif choice.lower() == "2":
        if doors > 1:
            os.system("clear")
            room()
            generation(r)


        else:
            print("You do not have 2 doors")
            choices()


    elif choice.lower() == "3":
        if doors > 2:
            os.system("clear")
            room()
            generation(r)

        else:
            print("You do not have 3 doors")
            choices()


    elif choice.lower() == "inventory" or choice.lower() == "inv":

        print("You have: " + "".join(inv))
        choices()


    elif choice.lower() == "use":
        if inv == False:
          print("You dont have anything in  your inventory!")
          choices()

        else:

          print("You can use anything in your inventory " + "".join(inv))
          useable = input("What would you like to use: ")

          if ("\n" + useable) in inv:
              use(useable, False)

          else:

              print("You do not have that item")
              choices()



    elif choice.lower() == "health":
        player.giveHealth()
        choices()



    else:
        print("that is not a valid option")
        choices()











def encounterChoice():

    if player.cHealth == 0 or 0 > player.cHealth:
        print(f"You ran out of health and died - you had £{player.money}")
        exit()




    global previous

    choice = input("> ")


    if choice.lower() == "run":

        didEscape = random.randint(1,100)
        if 30 > didEscape:
            damageDealt = random.randint(2,30)
            player.damageTook(damageDealt)
            print("While trying to escape and the monster followed you")
            encounterChoice()





        else:
            room()
            print("You ran and escaped to another room!")
            time.sleep(1)
            previous = True
            generation(r)


    elif choice.lower() == "use":

        if inv == False:
          print("You don't have anything in  your inventory!")
          encounterChoice()

        else:

          print("You can use anything in your inventory " + "".join(inv))
          useable = input("What would you like to use: ")

          if ("\n" + useable) in inv:
              use(useable, "enemy")

          else:

              print("You do not have that item")
              encounterChoice()



    elif choice.lower() == "fight":
        weaponInv = []
        for x in inv:

            weaponList = ["\nknife", "\nfork", "\nbat", "\ntorch", "\ncrowbar", "\nbranch", "\nshovel"]
            if x in weaponList:

                weaponInv.append(x)

        if weaponInv == []:
            damageTaken = random.randint(5,35)
            print(f"You don't have any weapons to attack with, and lost {damageTaken} health")
            player.cHealth -= damageTaken
            print("Pro tip - next time RUN if you don't have any weapons")
            encounterChoice()





        else:


            enemyhealth = 100
            firstTime = True
            while enemyhealth > 0:

                if player.cHealth == 0 or 0 > player.cHealth:
                    print(f"You ran out of health and died - you had {player.money} pounds")
                    exit()

                if firstTime == True:
                    print("you have:" + "".join(weaponInv))
                    firstTime = False
                weaponChoice = input("What weapon do you want to attack the enemy with? > ")
                print("")




                if ("\n" + weaponChoice) in weaponInv:


                    with open("weapons.json", "r") as f:
                        data = json.load(f)

                        Find = data["weapons"]
                        damageToEnemy = random.choice(Find[weaponChoice])
                        enemyhealth -= damageToEnemy
                        if enemyhealth == 0 or 0 > enemyhealth:
                            print(f"You did {damageToEnemy} to the enemy with your {weaponChoice} it now has 0 remaining")
                        else:
                            print(f"You did {damageToEnemy} to the enemy with your {weaponChoice}, the enemy now has {enemyhealth} health remaining")

                elif ("\n" + weaponChoice) not in weaponInv:
                    healthLost = random.randint(5, 35)
                    print(f"You spent too long looking for a weapon you don't have, and lost {healthLost} health")
                    encounterChoice()



                if enemyhealth > 0:
                    damageTaken = random.randint(1,20)
                    player.cHealth -= damageTaken
                    print(f"The enemy slashed you and dealt {damageTaken} damage. You now have {player.cHealth} health remaining")
                    print("")







            coinsLooted = random.randint(1,50)
            print(f"You killed the enemy and ran to another room, and looted £{coinsLooted}")
            player.money += coinsLooted
            time.sleep(2)
            room()
            generation(r)
            previous = True



    elif choice == "inv" or choice == "inventory":
        print("You have: " + "".join(inv))
        encounterChoice()




    elif choice.lower() == "health":
        player.giveHealth()
        encounterChoice()



    else:
        print("That is not a valid option!")
        encounterChoice()








def randomEncounter():

    os.system("clear")
    print("Uh Oh, you have come across an enemy!")
    print("you can RUN, FIGHT or USE an item.")
    encounterChoice()



def traderchoice():
    global food1,food2,weaponForSale
    global firstTime
    with open("shop.json", "r") as f:
        data = json.load(f)

        if firstTime == True:

            food1 = (random.choice(list(data["food"])))
            food2 = (random.choice(list(data["food"])))

            while food1 == food2:
                food2 = (random.choice(list(data["food"])))

            weaponChance = random.randint(1, 50)
            if weaponChance > 25:
                weaponForSale = (random.choice(list(data["weapons"])))



            firstTime = False
            traderchoice()


    choice = input("> ")

    if choice.lower() == "inv" or choice.lower() == "inventory":
        print("You have: " + "".join(inv))
        traderchoice()

    elif choice.lower() == "use":

        if inv == False:
            print("You don't have anything in  your inventory!")
            traderchoice()


        else:
          print("You can use anything in your inventory " + "".join(inv))
          useable = input("What would you like to use: ")


          if ("\n" + useable) in inv:
              use(useable, "trader")





          else:
                print("You do not have that item")

                traderchoice()




    elif choice.lower() == "shop":





            if firstTime == False:
                if weaponForSale == "":
                    print(f"The trader has:\n" + food1, "-", data["food"][food1])
                    print(food2, "-", data["food"][food2])
                else:
                    print(f"The trader has:\n" + food1, "-", data["food"][food1])
                    print(food2, "-", data["food"][food2])
                    print(weaponForSale, "-", data["weapons"][weaponForSale])


                traderchoice()

    elif choice.lower() == "leave":
        os.system("clear")
        room()
        generation(r)

    elif choice.lower() == "buy":
        food1Price = (data["food"][food1])
        food2Price = (data["food"][food2])
        weaponPrice = (data["weapons"][weaponForSale])
        if weaponForSale == "":
            print(f"The trader has:\n" + food1, "-", data["food"][food1])
            print(food2, "-", data["food"][food2])
        else:
            print(f"The trader has:\n" + food1, "-", data["food"][food1])
            print(food2, "-", data["food"][food2])
            print(weaponForSale, "-", data["weapons"][weaponForSale])

        print("You can buy anything listed as long as you have enough coins")
        tobuy = input("> ")
        if tobuy.lower() == food1:
            confirm = input(f"This costs £{food1Price}are you sure? y/n\n> ")
            if confirm == "y":
                player.money -= food1Price
                inv.append("\n" + food1)
                print(f"You now have £{player.money} remaining")
                traderchoice()


        elif tobuy.lower() == food2:
            confirm = input(f"This costs £{food2Price} are you sure? y/n\n> ")
            if confirm == "y":
              if player.money > food2Price or player.money == food2Price:
                  player.money -= food2Price
                  inv.append("\n" + food2)
                  print(f"You now have £{player.money} remaining")
                  traderchoice()
              else:
                print("You do not have enough money for this item.")
                traderchoice()

                
        elif tobuy.lower() == weaponForSale:
            confirm = input(f"This costs £{weaponPrice} are you sure? y/n\n> ")
            if confirm == "y":
              if player.money > food2Price or player.money == food2Price:
                  player.money -= food2Price
                  inv.append("\n" + food2)
                  print(f"You now have £{player.money} remaining")
                  traderchoice()
              else:
                print("You do not have enough money for this item.")
                traderchoice()

                


            else:
                traderchoice()

        else:
          traderchoice()











def traderEncounter():
    print("You have come across a wild trader, who is willing to sell items to you for a fee.")
    print("The trader will also play games with you, and you can earn (or loose) some money.")
    print("Use 'shop' to see what the trader has for sale, or use 'games' to gamble some money")
    traderchoice()

def generation(room):
    global firstTime
    firstTime = True
    hungerItems = ["waterbottle", "carrot", "tomato", "chocolate"]
    foodinv = []


    removeHunger = random.randint(1,100)
    if removeHunger > 50:
        hungerRemoved = random.randint(1,10)
        thirstRemoved = random.randint(1,10)

        player.thirst -= thirstRemoved
        player.hunger -= hungerRemoved

    elif player.hunger == 0 or player.hunger < 0 or player.thirst == 0 or player.thirst < 0:
        print("You ran out of hunger/thirst and died...")
        print("Game over!")


    elif player.hunger < 20 or player.thirst < 20:
        print("Your hunger and thirst levels are low. You should probably eat something")



    global previous
    traderRarity = random.randint(1,170)
    encounterChoice = random.randint(1,130)
    if 25 > encounterChoice and previous == False:
        encounter = True
    else:
        encounter = False
        previous = False
    if 20 > traderRarity:
        traderEnc = True
    else:
        traderEnc = False





    isTrue = True





    if encounter == True or encounter == True and traderEnc == True:
        randomEncounter()
    elif traderEnc == True and encounter == False:
        traderEncounter()




    elif isTrue == True and encounter == False and traderEnc == False:
        os.system("clear")
        realname = (r["RoomName"])


        print(f"you find yourself in a {realname} with {doors} door(s)")
        choices()



room()
startscreen()


