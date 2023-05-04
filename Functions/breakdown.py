def breakdown(ingredients,inv):
    passed = False
    for item in inv.craftingInv:
        if item == "\ngrindstone":
            passed = True
        else:
            pass
    if passed == False:
        print("You do not have a grindstone!")
        pass
    else:
        print("You can 'breakdown' your unused tools into scrap metal!")
        print("".join(inv.weaponInv))
        choice = input("> ")



    
    