import json




def breakdown(ingredients,inv):
    passed = False
    for item in inv.toolInv:
        if item == "\ngrindstone":
            passed = True
        else:
            pass
    if passed == False:
        print("You do not have a grindstone!")
        input()
        pass
    else:
        print("You can 'breakdown' your unused tools into scrap metal!")
        print("".join(inv.weaponInv))
        choice = input("> ")

        weaponList = ["\nknife", "\nfork", "\nbat",
                      "\ntorch", "\ncrowbar", "\nbranch", "\nshovel", "\nsword", "\nlongsword"]


        if ("\n" + choice) in weaponList:

            with open ("Json/weapons.json", "r") as f:
                data = json.load(f)
                find = data["breakdown"]

                metal = find[choice]
                if metal == True:
                    print(f"You cannot breakdowm {choice} into metal scrap!")
                    input()

                else:
                    for x in range(metal):
                        inv.inv.append("\nscrapmetal")

                    inv.inv.remove("\n" + choice)
                    print(f"Your {choice} broke down into {metal} metal scrap!")
                    input()


        else:
            print("Incorrect item!")
            input()



    
    