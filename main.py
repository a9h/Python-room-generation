import random
import json
import os
haslooted = False
r = ""
doors = 0
useable = ""
inv = ["\nmedicine"]

class character:
    def __init__(self, currentHealth, maxHealth):
        self.cHealth = currentHealth
        self.mHealth = maxHealth
    def giveHealth(self):
        print(f"Your current health is {self.cHealth} and your max health is {mHealth}")
        
player = character(100,100)

class regularenemy:
  def __init__(self, health, strength):
    self.health = health
    self.strength = strength

def CreateEnemy













class HealthPotion():
    def act(self, player):
        player.currentHealth += 20


def use(item):
    if item.lower() == "medicine":
        player.mHealth += 20
        print(f"Max health increased to {player.mHealth}")
        inv.remove("\n" + item)
        choices()
    elif item.lower() == "water":
        player.currentHealth += 5



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

    spots = ["You peaked in a cuboard", "You looked in a draw", "You opened a cabinate"]
    gathered = (random.choice(r["LootTables"]))
    

    if haslooted == False:
        if lucky < 33:
            haslooted = True
            print(f"{random.choice(spots)} and found {gathered}!")

            inv.append(f"\n{gathered}")
            choices()
                
        else:
            haslooted = True
            print("Looks like you didnt find anything, unlucky")
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
              use(useable)
          else:
              print("You do not have that item")
              choices()
    elif choice.lower() == "health":
        player.giveHealth()
        choices()


        
    else:
        print("that is not a valid option")
        choices()       








def generation(room):
    global doors
    isTrue = True
    if isTrue == True:
        os.system("clear")
        realname = (r["RoomName"])


        print(f"you find yourself in {realname} a  with {doors} door(s)")
        choices()



room()
startscreen()


