def buy(shop, data, player,inv):
    food1Price = (data["food"][shop.food1])
    food2Price = (data["food"][shop.food2])


    if shop.weapon == "":
        pass
    else:
        weaponPrice = (data["weapons"][shop.weapon])

    if shop.tool == "":
        pass
    else:
        toolPrice = (data["tools"][shop.tool])



    print("What would you like to purchase!")
    tobuy = input("> ")
    if tobuy.lower() == shop.food1:
        confirm = input(f"This costs £{food1Price} are you sure? y/n\n> ")
        if confirm == "y":
            if player.money > food1Price or player.money == food1Price:
                player.money -= food1Price
                inv.inv.append("\n" + shop.food1)
                print(f"You now have £{player.money} remaining")

            else:
                print("You do not have enough money for this item.")

    elif tobuy.lower() == shop.food2:
        confirm = input(f"This costs £{food2Price} are you sure? y/n\n> ")
        if confirm == "y":
            if player.money > food2Price or player.money == food2Price:
                player.money -= food2Price
                inv.inv.append("\n" + shop.food2)
                print(f"You now have £{player.money} remaining")

            else:
                print("You do not have enough money for this item.")

    elif tobuy.lower() == shop.weapon:
        confirm = input(f"This costs £{weaponPrice} are you sure? y/n\n> ")
        if confirm == "y":
            if player.money > weaponPrice or player.money == weaponPrice:
                player.money -= weaponPrice
                inv.inv.append("\n" + shop.weapon)
                print(f"You now have £{player.money} remaining")




    elif tobuy.lower() == shop.tool:
        confirm = input(f"This costs £{toolPrice} are you sure? y/n\n> ")
        if confirm == "y":
            if player.money >= toolPrice:
                player.money -= toolPrice
                inv.inv.append("\n" + shop.tool)
                print(f"You now have £{player.money} remaining")
            

            else:
                print("You do not have enough money for this item.")

        else:
            pass

    else:
        pass


