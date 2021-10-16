import random
import json
import os
haslooted = False
r = ""
doors = 0

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
    spots = ["You peaked in a cuboard", "You looked in a draw", "You opened a cabinate"]
    gathered = (random.choice(r["LootTables"]))
    
    lucky = random.randint(1,101)
    if haslooted == False:
        if lucky < 33:
            haslooted = True
            print(f"{random.choice(spots)} and found {gathered}!")

            with open ("inventory.json", "a") as f:
                json.dump(gathered, f, indent=4)
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


