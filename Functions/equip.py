#armour.head
#armour.chest
#armour.legs
import json




def equip(inv,armour):

    print("Armour:"+"".join(inv.armorInv))
    choice = input("> ")

    item = (choice)

    if ("\n" +choice) in inv.armorInv:
        with open ("Json/stats.json", "r") as f:
            data = json.load(f)

            if item in data["armour.head"]:
                head = data["armour.head"]
                armour.head += head[item]
                print(f"Head armour increased to {armour.head}")

            elif item in data["armour.chest"]:
                chest = data["armour.chest"]
                armour.chest += chest[item]
                print(f"Chest armour increased to {armour.chest}")

            elif item in data["armour.feet"]:
                feet = data["armour.feet"]
                armour.legs += feet[item]
                print(f"Leg armour increased to {armour.legs}")
            
        inv.inv.remove("\n" + item)

    else:
        print("incorrect item!")

            

            

