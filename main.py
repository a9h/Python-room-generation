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
enemy = ""
firstEnemy = True
previous = True
inv = ["\nmedicine"]


class character:
    def __init__(self, currentHealth, maxHealth, money, hunger, thirst, armour):
        self.cHealth = currentHealth
        self.mHealth = maxHealth
        self.money = money
        self.hunger = hunger
        self.thirst = thirst
        self.armour = armour


    def giveHealth(self):
        print(
            f"Your current health is {self.cHealth} and your max health is {self.mHealth}\nYour hunger is {self.hunger} and your thirst is {self.thirst}\nYou have £{self.money}")

    def damageTook(self, damage):
        self.cHealth -= damage
        if self.cHealth == 0 or self.cHealth < 0:
            print("Game over! you died")
            exit()
        else:
            print(f"You lost {damage} health, and now have {self.cHealth} left")


class weapon:
    def __init__(self, durability):
        self.durability = durability


knifeWeapon = weapon(150)
forkWeapon = weapon(40)
batWeapon = weapon(60)

player = character(100, 100, 50, 100, 100)





def use(item, encounter):
    with open("stats.json") as f, open("weapons.json") as b:
        data = json.load(f)
        wdata = json.load(b)

        if item in wdata["weapons"]:
            print("You cant use a weapon when there is no enemies to use it on")
            if encounter == "enemy":
                encounterChoice()

            elif encounter == "trader":
                traderchoice()
            else:
                choices()



        elif item in data["thirst"] and item in data["hunger"]:
            findThirst = data["thirst"]
            findHunger = data["hunger"]
            randomHunger = random.choice(findHunger[item])
            randomThirst = random.choice(findThirst[item])

            hungerDifference = 100 - player.hunger
            thirstDifference = 100 - player.thirst

            if randomThirst > thirstDifference:
                player.thirst += thirstDifference
                if player.thirst > 100:
                    player.thirst = 100
                else:
                    pass

            if randomHunger > hungerDifference:
                player.hunger += hungerDifference
                if player.hunger > 100:
                    player.hunger = 100
                else:
                    pass


            else:
                player.hunger += randomHunger
                player.thirst += randomThirst
            print(f"you used {item} and gained {randomHunger} hunger and {randomThirst} thirst")
            print(f"your current hunger and thirst levels are {player.hunger} and {player.thirst}")
            inv.remove("\n" + item)

            if encounter == "enemy":
                encounterChoice()

            elif encounter == "trader":
                traderchoice()
            else:
                choices()




        elif item in data["maxhealth"]:
            FindOption = data["maxhealth"]
            ToAdd = random.choice(FindOption[item])
            player.mHealth += ToAdd
            inv.remove("\n" + item)
            print(f"Max health increased to {player.mHealth}")
            if encounter == "enemy":
                encounterChoice()

            elif encounter == "trader":
                traderchoice()
            else:
                choices()

        elif item in data["currenthealth"]:
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
        doors = (random.randint(1, 3))


def loot(r):
    global haslooted
    global doors

    if doors == 1:
        lucky = random.randint(1, 101)


    elif doors == 2:
        lucky = random.randint(1, 76)

    elif doors == 3:
        lucky = random.randint(1, 51)

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

    elif choice.lower() == "drop":
        dropped = input("What item would you like to drop: ")

        if dropped in inv:
            inv.remove("\n" + dropped)
        else:
            print("You do not have that item...")
            choices()


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
    global enemy
    global firstEnemy

    if firstEnemy == True:
        enemyChance = random.randint(1,200)
        if enemyChance < 25:
            enemy = "hard"
        elif enemyChance > 25 and enemyChance < 125:
            enemy = "medium"
        elif enemyChance > 125:
            enemy = "easy"
        else:
            print("FATAL ERROR!")
        firstEnemy = False




    if enemy == "hard":
        enemyhealth = 250
        possibleDamage = random.randint(50,90)
    elif enemy == "easy":
        enemyhealth = 100
        possibleDamage = random.randint(2,25)
    elif enemy == "medium":
        enemyhealth = 150
        possibleDamage = random.randint(25,50)
    else:
        print("Fatal error")








    if player.cHealth == 0 or 0 > player.cHealth:
        print(f"You ran out of health and died - you had £{player.money}")
        exit()

    global previous
    print(f"The enemy is {enemy} with {enemyhealth} health")
    choice = input("> ")

    if choice.lower() == "run":
        didRun = False
        while didRun == False:

            didEscape = random.randint(1, 100)
            if 30 > didEscape:
                if enemy == "hard":
                    damageDealt = random.randint(50, 90)
                elif enemy == "medium":
                    damageDealt = random.randint(25, 50)
                elif enemy == "easy":
                    damageDealt = random.randint(2, 25)
                else:
                    print("Fatal error!")



                player.damageTook(damageDealt)
                print("While trying to escape and the monster followed you")
                input("> ")








            else:
                didRun = True
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


    elif choice.lower() == "drop":
        dropped = input("What item would you like to drop: ")

        if dropped in inv:
            inv.remove("\n" + dropped)
        else:
            print("You do not have that item...")
            encounterChoice()


    elif choice.lower() == "fight":
        weaponInv = []
        for x in inv:

            weaponList = ["\nknife", "\nfork", "\nbat", "\ntorch", "\ncrowbar", "\nbranch", "\nshovel"]
            if x in weaponList:
                weaponInv.append(x)

        if weaponInv == []:
            if enemy == "hard":
                damageTaken = random.randint(50, 90)
            elif enemy == "medium":
                damageTaken = random.randint(25, 50)
            elif enemy == "easy":
                damageTaken = random.randint(2, 25)
            else:
                print("Fatal error!")
            print(f"You don't have any weapons to attack with, and lost {damageTaken} health")
            player.cHealth -= damageTaken
            print("Pro tip - next time RUN if you don't have any weapons")
            encounterChoice()





        else:


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

                    if weaponChoice == "torch":
                        didScare = random.randint(1, 100)
                        if didScare < 25:
                            print("You light your torch and scare off the enemy!")
                            inv.remove("\ntorch")
                            room()
                            generation(r)
                        else:
                            print("The enemy did not care about your torch")

                    else:




                        with open("weapons.json", "r") as f:
                            data = json.load(f)

                            Find = data["weapons"]
                            damageToEnemy = random.choice(Find[weaponChoice])
                            enemyhealth -= damageToEnemy
                            if enemyhealth == 0 or 0 > enemyhealth:
                                print(
                                    f"You did {damageToEnemy} to the enemy with your {weaponChoice} it now has 0 remaining")
                            else:
                                print(
                                    f"You did {damageToEnemy} to the enemy with your {weaponChoice}, the enemy now has {enemyhealth} health remaining")

                elif item not in data["weapons"]:
                    if enemy == "hard":
                        healthLost = random.randint(50, 90)
                    elif enemy == "medium":
                        healthLost = random.randint(25, 50)
                    elif enemy == "easy":
                        healthLost = random.randint(2, 25)
                    else:
                        print("Fatal error!")

                    print(f"You spent too long looking for a weapon you don't have, and lost {healthLost} health")
                    encounterChoice()

                if enemyhealth > 0:
                    if enemy == "hard":
                        damageTaken = random.randint(50, 90)
                    elif enemy == "medium":
                        damageTaken = random.randint(25, 50)
                    elif enemy == "easy":
                        damageTaken = random.randint(2, 25)
                    else:
                        print("Fatal error!")
                    player.cHealth -= damageTaken
                    print(
                        f"The enemy slashed you and dealt {damageTaken} damage. You now have {player.cHealth} health remaining")
                    print("")

            coinsLooted = random.randint(1, 50)
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
    global food1, food2, weaponForSale
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


    elif choice.lower() == "drop":
        dropped = input("What item would you like to drop: ")

        if dropped in inv:
            inv.remove("\n" + dropped)
        else:
            print("You do not have that item...")
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


    elif choice.lower() == "health":
        player.giveHealth()
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
        if weaponForSale == "":
            pass
        else:
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
            confirm = input(f"This costs £{food1Price} are you sure? y/n\n> ")
            if confirm == "y":
                if player.money > food1Price or player.money == food1Price:
                    player.money -= food1Price
                    inv.append("\n" + food1)
                    print(f"You now have £{player.money} remaining")
                    traderchoice()
                else:
                    print("You do not have enough money for this item.")
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
                if player.money > weaponPrice or player.money == weaponPrice:
                    player.money -= weaponPrice
                    inv.append("\n" + weaponForSale)
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
    os.system("clear")
    print("You have come across a wild trader, who is willing to sell items to you for a fee.")
    print("The trader will also play games with you, and you can earn (or loose) some money.")
    print("Use 'shop' to see what the trader has for sale, or use 'games' to gamble some money")
    traderchoice()


def generation(room):
    global firstTime
    global firstEnemy
    global enemy
    enemy = ""
    firstEnemy = True
    firstTime = True
    hungerItems = ["waterbottle", "carrot", "tomato", "chocolate"]
    foodinv = []

    removeHunger = random.randint(1, 100)
    if removeHunger > 50:
        hungerRemoved = random.randint(1, 10)
        thirstRemoved = random.randint(1, 10)

        player.thirst -= thirstRemoved
        player.hunger -= hungerRemoved

    if player.hunger == 0 or player.hunger < 0 or player.thirst == 0 or player.thirst < 0:
        print("You ran out of hunger/thirst and died...")
        print("Game over!")
        exit()


    elif player.hunger < 20 or player.thirst < 20:
        print("Your hunger and thirst levels are low. You should probably eat something")

    global previous
    traderRarity = random.randint(1, 170)
    encounterChoice = random.randint(1, 130)
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
