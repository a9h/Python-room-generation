import random
import json
import os

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
    global doors
    global r  
    with open("rooms.json") as f:
        data = json.load(f)  
        r = random.choice(data["rooms"])
        doors = (random.randint(1,3))



def loot(r):
    spots = ["You peaked in a cuboard", "You looked in a draw", "You opened a cabinate"]
    gathered = (random.choice(r["LootTables"]))
    
    lucky = random.randint(1,101)
    
    if lucky < 33:
        print(f"{random.choice(spots)} and found {gathered}!")

        with open ("inventory.json", "a") as f:
            json.dump(gathered, f, indent=4)
            choices()
    else:
        print("Looks like you didnt find anything, unlucky")
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


