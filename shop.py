def buy(weaponForSale,food1,food2,data,player):
        food1Price = (data["food"][food1])
        food2Price = (data["food"][food2])
        if weaponForSale == "":
            pass
        else:
            weaponPrice = (data["weapons"][weaponForSale])

        if weaponForSale == "":
            print(f"The trader has:\n" + food1, "-", data["food"][food1])
            print(food2, "-", data["food"][food2])



        else:
            print(f"The trader has:\n" + food1, "-", data["food"][food1])
            print(food2, "-", data["food"][food2])
            print(weaponForSale, "-", data["weapons"][weaponForSale])

        print("You can buy anything listed as long as you have enough coins")
        tobuy = input("> ")
        if tobuy.lower() == food1:
            confirm = input(f"This costs £{food1Price} are you sure? y/n\n> ")
            if confirm == "y":
                if player.money > food1Price or player.money == food1Price:
                    player.money -= food1Price
                    player.inv.append("\n" + food1)
                    print(f"You now have £{player.money} remaining")

                else:
                    print("You do not have enough money for this item.")


        elif tobuy.lower() == food2:
            confirm = input(f"This costs £{food2Price} are you sure? y/n\n> ")
            if confirm == "y":
                if player.money > food2Price or player.money == food2Price:
                    player.money -= food2Price
                    player.inv.append("\n" + food2)
                    print(f"You now have £{player.money} remaining")

                else:
                    print("You do not have enough money for this item.")



        elif tobuy.lower() == weaponForSale:
            confirm = input(f"This costs £{weaponPrice} are you sure? y/n\n> ")
            if confirm == "y":
                if player.money > weaponPrice or player.money == weaponPrice:
                    player.money -= weaponPrice
                    player.inv.append("\n" + weaponForSale)
                    print(f"You now have £{player.money} remaining")

                else:
                    print("You do not have enough money for this item.")
                    




            else:
                pass


        else:
            pass
