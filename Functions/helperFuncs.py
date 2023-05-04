from collections import Counter
import json
import os



        

def craftingConvert(inv,ingredients):
    counter = 0
    counter2 = 0
    for item in inv.inv:


        if item == "\nscrapmetal":
            counter +=1

        elif item == "\niron":
            counter2 += 1


        else:
            pass

    ingredients.metal = counter
    ingredients.iron = counter2





        













def sortinv(player, inv,ingredients,armour):

    total = armour.head + armour.chest + armour.legs

    armour.total = total/3

    armour.total = round(armour.total)




    craftingConvert(inv=inv,ingredients=ingredients)
    if player.thirst > 100 or player.hunger > 100:
        player.thirst = 100
        player.hunger = 100


    



    counts = dict(Counter(inv.inv))
    duplicates = {key:value for key, value in counts.items() if value > 1}
    inv.weaponInv = [""]
    inv.craftingInv = [""]
    inv.consumableInv = [""]
    inv.healthInv = [""]
    inv.armorInv = [""]
    inv.toolInv = [""]
    with open("Json/itemLists.json", "r") as f:
    
        data = json.load(f)


        for duplicate, count in duplicates.items():
            for item in inv.inv:

                if item != duplicate:




                    if item in data["weaponList"]:
                        inv.weaponInv.append(item)
                 

                    elif item in data["craftingList"]:

                        inv.craftingInv.append(item)
                    
                    elif item in data["consumableList"]:
                        inv.consumableInv.append(item)
                   

                    elif item in data["healthList"]:
                        inv.healthInv.append(item)
                    elif item in data["armorList"]:
                        inv.armorInv.append(item)
                    elif item in data["toolList"]:
                        inv.toolInv.append(item)



                    else:
                        print("maderror")
                    

                else:


                    if item in data["weaponList"]:
                        inv.weaponInv.append(f"{duplicate} x{count}")




                    elif item in data["craftingList"]:

                        inv.craftingInv.append(f"{duplicate} x{count}")

                    
                    elif item in data["consumableList"]:
                        inv.consumableInv.append(f"{duplicate} x{count}")



                    elif item in data["healthList"]:
                        inv.healthInv.append(f"{duplicate} x{count}")

                    elif item in data["armorList"]:
                        inv.armorInv.append(f"{duplicate} x{count}")

                    elif item in data["toolList"]:
                        inv.toolInv.append(item)

                    else:
                        print("mad error")
    
    uniqueW = list(set(inv.weaponInv))
    inv.weaponInv = uniqueW

    for item in inv.weaponInv:
        for num in range(100):
            if (item+f" x{num}") in inv.weaponInv:
                inv.weaponInv.remove(item)
            else:
                pass

    uniqueT = list(set(inv.toolInv))
    inv.toolInv = uniqueT

    for item in inv.toolInv:
        for num in range(100):
            if (item+f" x{num}") in inv.toolInv:
                inv.toolInv.remove(item)
            else:
                pass







    uniqueA = list(set(inv.armorInv))
    inv.armorInv = uniqueA

    for item in inv.armorInv:
        for num in range(100):
            if (item+f" x{num}") in inv.armorInv:
                inv.armorInv.remove(item)
            else:
                pass



    uniqueCr = list(set(inv.craftingInv))
    inv.craftingInv = uniqueCr

    for item in inv.craftingInv:
        for num in range(100):
            if (item+f" x{num}") in inv.craftingInv:
                inv.craftingInv.remove(item)
            else:
                pass



    uniqueC = list(set(inv.consumableInv))
    inv.consumableInv = uniqueC


    for item in inv.consumableInv:
        for num in range(100):
            if (item+f" x{num}") in inv.consumableInv:
                inv.consumableInv.remove(item)
            else:
                pass
            

    uniqueH = list(set(inv.healthInv))
    inv.healthInv = uniqueH
    for item in inv.healthInv:
        for num in range(100):
            if (item+f" x{num}") in inv.healthInv:
                inv.healthInv.remove(item)
            else:
                pass









                        


def inventory():

        os.system("clear")
        print("""
╔════════════════════════════════════════════╗    
║ ╦  ╔╗╔  ╦  ╦  ╔═╗  ╔╗╔  ╔╦╗  ╔═╗  ╦═╗  ╦ ╦ ║ 
║ ║  ║║║  ╚╗╔╝  ║╣   ║║║   ║   ║ ║  ╠╦╝  ╚╦╝ ║
║ ╩  ╝╚╝   ╚╝   ╚═╝  ╝╚╝   ╩   ╚═╝  ╩╚═   ╩  ║
╚════════════════════════════════════════════╝
    """)
        
        print("Use < & > to cycle through categories")

    




def printinv(inv,ingredients,player,armour):
    inventory()



    counter = 0

    print("""
Consumables
═══════════
    """ + "".join(inv.consumableInv))

    exit = "False"

    while exit == "False":
        print("")
        cycle = input("> ")

        if cycle == ">":
            if counter + 1 > 5:
                counter = 0
            else:
                counter = counter +1

            match counter:

                    case 0:
                        inventory()
                        print("""
Consumables
═══════════
            """ + "".join(inv.consumableInv))
                        
                    case 1:
                        inventory()
                        print("""
Weapons
═══════
            """ + "".join(inv.weaponInv))
                        
                    case 2:
                        inventory()
                        print("""
Healables
═════════
            """ + "".join(inv.healthInv))
                    
                    case 3:
                        inventory()
                        print("""
Crafting
════════
            """ + "".join(inv.craftingInv))
                        
                    
                    case 4:
                        inventory()
                        print("""
Armour
══════
            """ + "".join(inv.armorInv))
                        

                    case 5:
                        inventory()
                        print("""
Tools
═════
            """ + "".join(inv.toolInv))

                    

        elif cycle == "<":
            if counter - 1 < 0:
                counter = 5
            else:
                counter = counter - 1
            match counter:

                    case 0:
                        inventory()
                        print("""
Consumables
═══════════
            """ + "".join(inv.consumableInv))
                        
                    case 1:
                        inventory()
                        print("""
Weapons
═══════
            """ + "".join(inv.weaponInv))
                        
                    case 2:
                        inventory()
                        print("""
Healables
═════════
            """ + "".join(inv.healthInv))
                    
                    case 3:
                        inventory()
                        print("""
Crafting
════════
            """ + "".join(inv.craftingInv))
                        
                    
                    case 4:
                        inventory()
                        print("""
Armour
══════
            """ + "".join(inv.armorInv))
                        
                    case 5:
                        inventory()
                        print("""
Tools
═════
            """ + "".join(inv.toolInv))
                        
                    

                        
        elif cycle == "exit":
            os.system("clear")
            exit = True
            pass



        elif cycle == "drop":
            dropped = input("What item would you like to drop: ")

            if ("\n" + dropped) in inv.inv:
                inv.inv.remove("\n" + dropped)
                sortinv(armour=armour,ingredients=ingredients,inv=inv,player=player)
                os.system("clear")
                print(f"Dropped {dropped}")
                input()

            else:
                print("You do not have that item...")
                input()
                printinv






            




