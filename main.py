import random
import json
import time
import os
from pystyle import Write, Colors


from Functions.helperFuncs import sortinv, printinv
from Functions.use import use
from Functions.shop import buy
from Functions.fight import fight
from Functions.games import games
from Functions.admin import admin
from Functions.crafting import crafting
from Functions.equip import equip
from Functions.breakdown import breakdown






enemy = ""
firstEnemy = True
previous = True



















class shop1:
    def __init__(self,food1,food2,weapon,firstTime,tool) -> None:

        self.food1 = food1
        self.food2 = food2
        self.weapon = weapon
        self.firstTime = firstTime
        self.tool = tool


    def loadShop(self):
            with open("Json/shop.json", "r") as f:
                data = json.load(f)

                self.food1 = (random.choice(list(data["food"])))
                self.food2 = (random.choice(list(data["food"])))



                while shop.food1 == shop.food2:
                    self.food2 = (random.choice(list(data["food"])))

                toolChance =  random.randint(1,100)
                if toolChance <100:
                    self.tool = random.choice(list(data["tools"]))

                

                weaponChance = random.randint(1, 50)
                if weaponChance > 25:
                    self.weaponForSale = (random.choice(list(data["weapons"])))

                self.firstTime = False


















class ingredient:
    def __init__(self,metal,iron) -> None:
        self.metal = metal
        self.iron = iron







class armour:
    def __init__(self,head,chest,legs,total) -> None:
        self.head = head
        self.chest = chest
        self.legs = legs
        
        self.total = total



    def printarmour(self):

        print(fr"""
     ___
    |. .| <---{self.head}
    |[-]|
   /#####\
  //#####\\     <---{self.chest}
 // ##### \\
    ^^^^^  
    | | |
    |_|_| <---{self.legs}
    [ | ]""")
        print(f"armour will reduce damage by %{self.total}")

        input()
        os.system("clear")





class generation:
    def __init__(self, doors, room,realname):
        self.doors = doors
        self.room = room
        self.realname = realname







class character:
    def __init__(self, currentHealth, maxHealth, money, hunger, thirst, haslooted):
        self.cHealth = currentHealth

        self.mHealth = maxHealth

        self.money = money

        self.hunger = hunger

        self.thirst = thirst

        self.haslooted = haslooted







    def giveHealth(self):
        os.system("clear")
        Write.Print(f"""
╔════════╗ ╔════════════╗   ╔════════╗ ╔════════╗
║ health ║ ║ max health ║   ║ hunger ║ ║ thirst ║ 
║  {self.cHealth}   ║ ║    {self.mHealth}     ║   ║  {self.hunger}    ║ ║   {self.thirst}   ║        
╚════════╝ ╚════════════╝   ╚════════╝ ╚════════╝
           ╔═════════════════════════╗
           ║          money          ║                              
           ║           ${self.money}           ║
           ╚═════════════════════════╝
        
""",Colors.white, interval=0.005)
        input()
        os.system("clear")







    def damageTook(self, damage):
        self.cHealth -= damage
        if self.cHealth == 0 or self.cHealth < 0:
            print("Game over! you died")
            exit()
        else:
            print(
                f"You lost {damage} health, and now have {self.cHealth} left")



class inventory:
    def __init__(self,inv, weaponInv, craftingInv, 
                 consumableInv, healthInv,armorInv,toolInv) -> None:
        

        self.inv = inv



        self.weaponInv = weaponInv

        self.craftingInv = craftingInv

        self.consumableInv = consumableInv

        self.healthInv = healthInv
        
        self.armorInv = armorInv

        self.toolInv = toolInv





shop = shop1("","","",True,"")




inv = inventory(["\nmedicine", "\nmedicine"], 
[""],[""],[""],[""], [""], "")




armour = armour(0,0,0,0)


ingredients = ingredient(0,0)


player = character(100, 100, 50, 100, 100, False, 
)
generator = generation(0, "", "")




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
    os.system("clear")
    Write.Print("""
      ╦  ╔═╗╔═╗╔╦╗
      ║  ║ ║╚═╗ ║ 
      ╩═╝╚═╝╚═╝ ╩    
╔═══════════════════════════════════╗
║         Welcome to lost           ║
║ Do you have a save to load? (y/n) ║ 
╚═══════════════════════════════════╝
""",Colors.white, interval=0.005)
    choice = input("> ")

    match choice:

        case  "y":
            with open("Json/save.json", "r") as f:

                data = json.load(f)

                player.cHealth = data["cHealth"]
                player.mHealth = data["mHealth"]
                player.money = data["money"]
                player.hunger = data["hunger"]
                player.thirst = data["thirst"]
                inv.inv = data["inv"]
                inv.consumableInv = data["consumableInv"]
                inv.craftingInv = data["craftingInv"]
                inv.healthInv = data["healthInv"]
                inv.weaponInv = data["weaponInv"]
                ingredients.iron = data["iron"]
                ingredients.metal = data["metal"]
                inv.armorInv = data["armorInv"]

                armour.head = data["head"]
                armour.chest = data["chest"]
                armour.legs = data["legs"]

                inv.toolInv = data["tools"]
                

                print("save.json successfully loaded")
                input("")

        case "n":
            pass

        case _:
            pass

                


            



    os.system("clear")
    generation()


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

    spots = ["You peeked in a cupboard",
             "You looked in a drawer", "You opened a cabinet"]
    gathered = (random.choice(generator.room["LootTables"]))

    if player.haslooted == False:
        if lucky < 33:
            player.haslooted = True
            
            key = random.randint(1,125)

            if key > 50:
                money = 0
            elif key < 50 and key < 100:
                money = random.randint(15,25)
            elif key > 100:
                money = random.randint(25,40)
            else:
                money = 0




            if money == 0:
                print(f"{random.choice(spots)} and found {gathered}")
            else:
                print(f"{random.choice(spots)} and found {gathered} & £{money}!")



            inv.inv.append(f"\n{gathered}")
            player.money = player.money + money
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

    sortinv(player=player, inv=inv,ingredients=ingredients,armour=armour)

    choice = input("> ")
    choice = choice.lower()
    match choice:

        case "loot":
            loot()

        case "drop":
            dropped = input("What item would you like to drop: ")

            if ("\n" + dropped) in inv.inv:
                inv.inv.remove("\n" + dropped)
                sortinv(armour=armour,ingredients=ingredient,inv=inv,player=player)
                print(f"Dropped {dropped}")
                choices()
            else:
                print("You do not have that item...")
                input()
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
            sortinv(player=player,inv=inv,ingredients=ingredients,armour=armour)
            printinv(player=player,inv=inv,ingredients=ingredients,armour=armour)
            choices()

        case "admin":
            admin(player=player,inv=inv)
            choices()


        case "crafting":
            crafting(inv=inv,ingredients=ingredients)
            choices()

        case "use":
            if inv.inv == False:
                print("You dont have anything in  your inventory!")
                choices()

            else:

                print("You can use anything in your inventory " +
                      "".join(inv.healthInv)+"".join(inv.consumableInv))
                useable = input("What would you like to use: ")

                if ("\n" + useable) in inv.inv:
                    use(useable, False, player=player,inv=inv)
                    sortinv(player=player,inv=inv,ingredients=ingredients,armour=armour)
                    choices()

                else:

                    print("You do not have that item")
                    choices()

        case "equip":
            if inv.armorInv == [""]:
                print("You have nothing to equip")
            else:
                equip(inv=inv,armour=armour)
                choices()


        case "armour":
            armour.printarmour()
            choices()


        case "health":
            player.giveHealth()
            choices()

        case "save":
            print("this will overwrite all other saves - proceed? y/n")

            proceed = input("> ")

            match proceed:

                case "y":

                    f = open("Json/save.json", "w")

                    dictionary = {
                        "cHealth": player.cHealth,
                        "mHealth": player.mHealth,
                        "money": player.money,
                        "hunger": player.hunger,
                        "thirst": player.thirst,
                        "inv": inv.inv,
                        "consumableInv" : inv.consumableInv,
                        "craftingInv":inv.craftingInv, 
                        "healthInv":inv.healthInv, 
                        "weaponInv":inv.weaponInv, 
                        "metal": ingredients.metal,
                        "iron": ingredients.iron,
                        "armorInv" : inv.armorInv,
                        "head" : armour.head,
                        "chest" : armour.chest,
                        "legs" : armour.legs,
                        "tools" : inv.toolInv

                    }

                    json_object = json.dumps(dictionary, indent=4)

                    with open("Json/save.json", "w") as outfile:
                        outfile.write(json_object)
                    print("game saved")

                    choices()

                case "n":   

                    choices()

                case _:
                    choices()

        case "breakdown":
            breakdown(inv=inv,ingredients=ingredient)
            os.system("clear")
            choices()



                

        case "load":
            with open("Json/save.json", "r") as f:

                data = json.load(f)

                player.cHealth = data["cHealth"]
                player.mHealth = data["mHealth"]
                player.money = data["money"]
                player.hunger = data["hunger"]
                player.thirst = data["thirst"]
                inv.inv = data["inv"]
                inv.consumableInv = data["consumableInv"]
                inv.craftingInv = data["craftingInv"]
                inv.healthInv = data["healthInv"]
                inv.weaponInv = data["weaponInv"]
                ingredients.iron = data["iron"]
                ingredients.metal = data["metal"]
                inv.armorInv = data["armorInv"]
                armour.head = data["head"]
                armour.chest = data["chest"]
                armour.legs = data["legs"]
                inv.toolInv = data["tools"]

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

            if inv.inv == False:
                print("You don't have anything in  your inventory!")
                encounterChoice()

            else:

                print("You can use anything in your inventory " +
                      "".join(inv.healthInv)+"".join(inv.consumableInv))
                useable = input("What would you like to use: ")

                if ("\n" + useable) in inv.inv:
                    use(useable, "enemy", player=player, inv=inv)
                    sortinv(player=player,inv=inv,ingredients=ingredients,armour=armour)
                    encounterChoice()

                else:

                    print("You do not have that item")
                    encounterChoice()

        case "drop":
            dropped = input("What item would you like to drop: ")

            if dropped in inv.inv:
                inv.inv.remove("\n" + dropped)
            else:
                print("You do not have that item...")
                encounterChoice()

        case "fight":
            fight(player=player, enemy=enemy, enemyhealth=enemyhealth, inv=inv,armour=armour)
            time.sleep(2)
            room()
            generation()
            previous = True

        case "inv":
            sortinv(player=player,inv=inv,ingredients=ingredients,armour=armour)
            printinv(player=player,inv=inv,ingredients=ingredients,armour=armour)

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




    if shop.firstTime == True:
            shop.loadShop()

            traderchoice()

    choice = input("> ")

    match choice:
        case "inv":
            sortinv(player=player,inv=inv,ingredients=ingredients,armour=armour)
            printinv(player=player,inv=inv,ingredients=ingredients,armour=armour)
            traderchoice()

        case "drop":
            dropped = input("What item would you like to drop: ")

            if dropped in inv.inv:
                inv.inv.remove("\n" + dropped)
            else:
                print("You do not have that item...")
                traderchoice()

        case "use":

            if inv.inv == False:
                print("You don't have anything in  your inventory!")
                traderchoice()

            else:
                print("You can use anything in your inventory " +
                      "".join(inv.healthInv)+"".join(inv.consumableInv))
                useable = input("What would you like to use: ")

                if ("\n" + useable) in inv.inv:
                    
                    use(useable, "trader", player=player,inv=inv)
                    sortinv(player=player, inv=inv,ingredients=ingredients,armour=armour)

                else:
                    print("You do not have that item")

                    traderchoice()

        case "health":
            player.giveHealth()
            traderchoice()

        case "shop":

            if shop.firstTime == False:
                with open ("Json/shop.json", "r") as f:
                    data = json.load(f)
                    if shop.weapon == "":
                        print(f"The trader has:\n" + shop.food1,
                            "-", data["food"][shop.food1])
                        print(shop.food2, "-", data["food"][shop.food2])
                        if shop.tool == "":
                            pass
                        else:
                            print(shop.tool, "-", data["tools"][shop.tool])




                    else:
                        print(f"The trader has:\n" + shop.food1,
                            "-", data["food"][shop.food1])
                        print(shop.food2, "-", data["food"][shop.food2])
                        print(shop.weapon), "-", data["weapons"][shop.weapon]
                        if shop.tool == "":
                            pass
                        else:
                            print(shop.tool, "-", data["tool"][shop.tool])


                traderchoice()

        case "leave":
            shop.firstTime = True
            os.system("clear")
            room()
            generation()

        case "buy":
            with open ("Json/shop.json", "r") as f:
                data = json.load(f)
                buy(shop=shop, data=data, player=player,inv=inv)
                traderchoice()

        case "games":
            games(player=player)
            traderEncounter()

        case _:
            print("That is not a valid option")
            traderchoice()


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
        generator.realname = realname
        Write.Print(f"""you find yourself in a {realname} with {generator.doors} door(s)
""", Colors.white, interval=0.005)
        choices()


room()
startscreen()
