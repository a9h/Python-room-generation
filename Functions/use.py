
import random
import json










def use(item, encounter, player,inv):
    with open("Json/stats.json") as f, open("Json/weapons.json") as b:
        data = json.load(f)
        wdata = json.load(b)

        if item in wdata["weapons"]:
            print("You cant use a weapon when there is no enemies to use it on")



        elif item in data["thirst"] and item in data["hunger"]:
            findThirst = data["thirst"]
            findHunger = data["hunger"]
            randomHunger = random.choice(findHunger[item])
            randomThirst = random.choice(findThirst[item])





            player.hunger += randomHunger
            player.thirst += randomThirst

            if player.hunger > 100:
                player.hunger = 100
            if player.thirst > 100:
                player.thirst = 100

            
                
            print(f"you used {item} and gained {randomHunger} hunger and {randomThirst} thirst")
            print(f"your current hunger and thirst levels are {player.hunger} and {player.thirst}")
            inv.inv.remove("\n" + item)






        elif item in data["maxhealth"]:
            FindOption = data["maxhealth"]
            ToAdd = random.choice(FindOption[item])
            player.mHealth += ToAdd
            inv.inv.remove("\n" + item)
            print(f"Max health increased to {player.mHealth}")


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

            inv.inv.remove("\n" + item)

