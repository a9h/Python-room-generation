import random
import json
import time
import os

from helperFuncs import sortinv
from use import use
from shop import buy
from fight import fight
from games import games


food1 = ""
food2 = ""
weaponForSale = ""


enemy = ""
firstEnemy = True
previous = True


class generation:
    def __init__(self, doors, room):
        self.doors = doors
        self.room = room


class character:
    def __init__(self, currentHealth, maxHealth, money, hunger, thirst, haslooted, inv, printinv):
        self.cHealth = currentHealth

        self.mHealth = maxHealth

        self.money = money

        self.hunger = hunger

        self.thirst = thirst

        self.haslooted = haslooted

        self.inv = inv

        self.printinv = printinv

    def giveHealth(self):
        print(
            f"Your current health is {self.cHealth} and your max health is {self.mHealth}\nYour hunger is {self.hunger} and your thirst is {self.thirst}\nYou have £{self.money}")

    def damageTook(self, damage):
        self.cHealth -= damage
        if self.cHealth == 0 or self.cHealth < 0:
            print("Game over! you died")
            exit()
        else:
            print(
                f"You lost {damage} health, and now have {self.cHealth} left")


class weapon:
    def __init__(self, durability):
        self.durability = durability


knifeWeapon = weapon(150)
forkWeapon = weapon(40)
batWeapon = weapon(60)

player = character(100, 100, 50, 100, 100, False, [
                   "\nmedicine", "\nmedicine", "\nd"], [""])
generator = generation(0, "")


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
        generation()


def startscreen():
    print("Type 'help' for a list of commands or 'play' to start")
    startchoice()


# "Create" current room
def room():

    with open("Json/rooms.json") as f:
        player.haslooted = False
        data = json.load(f)
        generator.room = random.choice(data["rooms"])
        generator.doors = random.randint(1, 3)




def loot():

    if generator.doors == 1:
        lucky = random.randint(1, 101)

    elif generator.doors == 2:
        lucky = random.randint(1, 76)

    elif generator.doors == 3:
        lucky = random.randint(1, 51)

    spots = ["You peaked in a cupboard",
             "You looked in a draw", "You opened a cabinet"]
    gathered = (random.choice(generator.room["LootTables"]))

    if player.haslooted == False:
        if lucky < 33:
            player.haslooted = True
            print(f"{random.choice(spots)} and found {gathered}!")

            player.inv.append(f"\n{gathered}")
            choices()

        else:
            player.haslooted = True
            print("Looks like you didn't find anything, unlucky")
            choices()
    else:
        print("You have already looted this room!")
        choices()


# room()
# generation(r)


def choices():
    sortinv(player=player)

    choice = input("> ")
    choice = choice.lower()
    match choice:

        case "loot":
            loot()

        case "drop":
            dropped = input("What item would you like to drop: ")

            if dropped in player.inv:
                player.inv.remove("\n" + dropped)
            else:
                print("You do not have that item...")
                choices()

        case "help":
            print("help - shows this menu")
            print("loot - look around your room for anything useful")
            print("1 - goes through door 1 ")
            print("2 - goes through door 2 (If you have 2 doors available) ")
            print("3 - goes through door 2 (If you have 3 doors available) ")
            choices()

        case "1":
            os.system("clear")
            room()
            generation()

        case "2":
            if generator.doors > 1:
                os.system("clear")
                room()
                generation()

            else:
                print("You do not have 2 doors")
                choices()

        case "3":
            if generator.doors > 2:
                os.system("clear")
                room()
                generation()

            else:
                print("You do not have 3 doors")
                choices()

        case "inv":
            sortinv(player=player)
            print("You have: " + "".join(player.printinv))
            choices()

        case "use":
            if player.inv == False:
                print("You dont have anything in  your inventory!")
                choices()

            else:

                print("You can use anything in your inventory " +
                      "".join(player.printinv))
                useable = input("What would you like to use: ")

                if ("\n" + useable) in player.inv:
                    use(useable, False, player=player)
                    sortinv(player=player)
                    choices()

                else:

                    print("You do not have that item")
                    choices()

        case "health":
            player.giveHealth()
            choices()

        case "save":
            print("this will overwrite all other saves - proceed? y/n")

            proceed = input("> ")

            match proceed:

                case "y":

                    f = open("save.json", "w")

                    dictionary = {
                        "cHealth": player.cHealth,
                        "mHealth": player.mHealth,
                        "money": player.money,
                        "thirst": player.thirst,
                        "inv": player.inv,
                        "printinv": player.printinv

                    }

                    json_object = json.dumps(dictionary, indent=4)

                    with open("save.json", "w") as outfile:
                        outfile.write(json_object)
                    print("game saved")
                    choices()

                case "n":
                    choices()

                case _:
                    choices()

        case "load":
            with open("save.json", "r") as f:

                data = json.load(f)

                player.cHealth = data["cHealth"]
                player.mHealth = data["mHealth"]
                player.money = data["money"]
                player.hunger = data["hunger"]
                player.thirst = data["thirst"]
                player.inv = data["inv"]
                player.printinv = data["printinv"]

                print("save.json successfully loaded")

                choices()

        case _:
            print("that is not a valid option")
            choices()


def encounterChoice():
    global enemy
    global firstEnemy

    if firstEnemy == True:
        enemyChance = random.randint(1, 200)

        if enemyChance < 25:
            enemy = "hard"
            enemyhealth = 250

        elif enemyChance > 25 and enemyChance < 125:
            enemy = "medium"
            enemyhealth = 150

        elif enemyChance > 125:
            enemy = "easy"
            enemyhealth = 100

        else:
            print("FATAL ERROR!")
        firstEnemy = False

    match enemy:
        case "hard":
            enemyhealth = 250

        case "easy":
            enemyhealth = 100

        case "medium":
            enemyhealth = 150

    if player.cHealth == 0 or 0 > player.cHealth:
        print(f"You ran out of health and died - you had £{player.money}")
        exit()

    global previous
    print(f"The enemy is {enemy} with {enemyhealth} health")
    choice = input("> ")

    match choice:

        case "run":
            didRun = False
            while didRun == False:

                didEscape = random.randint(1, 100)
                if 30 > didEscape:

                    match enemy:

                        case "hard":
                            damageDealt = random.randint(50, 90)
                        case "medium":
                            damageDealt = random.randint(25, 50)
                        case "easy":
                            damageDealt = random.randint(2, 25)
                        case _:
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
                    generation()

        case "use":

            if player.inv == False:
                print("You don't have anything in  your inventory!")
                encounterChoice()

            else:

                print("You can use anything in your inventory " +
                      "".join(player.inv))
                useable = input("What would you like to use: ")

                if ("\n" + useable) in player.inv:
                    use(useable, "enemy", player=player)
                    sortinv(player=player)

                else:

                    print("You do not have that item")
                    encounterChoice()

        case "drop":
            dropped = input("What item would you like to drop: ")

            if dropped in player.inv:
                player.inv.remove("\n" + dropped)
            else:
                print("You do not have that item...")
                encounterChoice()

        case "fight":
            fight(player=player, enemy=enemy, enemyhealth=enemyhealth)
            time.sleep(2)
            room()
            generation()
            previous = True

        case "inv":
            sortinv(player=player)
            print("You have: " + "".join(player.printinv))
            encounterChoice()

        case "health":
            player.giveHealth()
            encounterChoice()

        case _:
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
    with open("Json/shop.json", "r") as f:
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

    match choice:
        case "inv":
            sortinv(player=player)
            print("You have: " + "".join(player.printinv))
            traderchoice()

        case "drop":
            dropped = input("What item would you like to drop: ")

            if dropped in player.inv:
                player.inv.remove("\n" + dropped)
            else:
                print("You do not have that item...")
                traderchoice()

        case "use":

            if player.inv == False:
                print("You don't have anything in  your inventory!")
                traderchoice()

            else:
                print("You can use anything in your inventory " +
                      "".join(player.inv))
                useable = input("What would you like to use: ")

                if ("\n" + useable) in player.inv:
                    
                    use(useable, "trader", player=player)
                    sortinv(player=player)

                else:
                    print("You do not have that item")

                    traderchoice()

        case "health":
            player.giveHealth()
            traderchoice()

        case "shop":

            if firstTime == False:
                if weaponForSale == "":
                    print(f"The trader has:\n" + food1,
                          "-", data["food"][food1])
                    print(food2, "-", data["food"][food2])
                else:
                    print(f"The trader has:\n" + food1,
                          "-", data["food"][food1])
                    print(food2, "-", data["food"][food2])
                    print(weaponForSale, "-", data["weapons"][weaponForSale])

                traderchoice()

        case "leave":
            os.system("clear")
            room()
            generation()

        case "buy":
            buy(weaponForSale=weaponForSale, food1=food1,
                food2=food2, data=data, player=player)
            traderchoice()

        case "games":
            games(player=player)
            traderEncounter()


def traderEncounter():
    os.system("clear")
    print("You have come across a wild trader, who is willing to sell items to you for a fee.")
    print("The trader will also play games with you, and you can earn (or loose) some money.")
    print("Use 'shop' to see what the trader has for sale, or use 'games' to gamble some money")
    traderchoice()


def generation():
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
        realname = (generator.room["RoomName"])

        print(
            f"you find yourself in a {realname} with {generator.doors} door(s)")
        choices()


room()
startscreen()
