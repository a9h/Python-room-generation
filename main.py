import random
import json
import os




# "Create" current room
with open("rooms.json") as f:
    data = json.load(f)
    
    r = random.choice(data["rooms"])



def loot(r):
    spots = ["You peaked in a cubard", "You looked in a draw", "You opened a cabinate"]
    gathered = (random.choice(r["LootTables"]))
    
    print(f"{random.choice(spots)} and found {gathered}!")

    with open ("inventory.json", "a") as f:
        json.dump(gathered, f, indent=4)


    


def choices():
    choice = input("> ")
    if choice == "loot":
        loot(r)





def generation(room):
    
    os.system("clear")
    doors = (random.randint(1,3))
    print(room)


    print(f"you find yourself in  a  with {doors} door(s)")
    choices()




generation(r)


