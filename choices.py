from main import *
import os

def choices():
    global useable
    global doors
    choice = input("> ")

    if choice.lower() == "loot":
        loot(r)

    elif choice.lower() == "drop":
        dropped = input("What item would you like to drop: ")

        if dropped in player.inv:
            player.inv.remove("\n" + dropped)
        else:
            print("You do not have that item...")
            choices()


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


    elif choice.lower() == "inventory" or choice.lower() == "inv":

        print("You have: " + "".join(player.inv))
        choices()


    elif choice.lower() == "use":
        if player.inv == False:
            print("You dont have anything in  your inventory!")
            choices()

        else:

            print("You can use anything in your inventory " + "".join(player.inv))
            useable = input("What would you like to use: ")

            if ("\n" + useable) in player.inv:
                use(useable, False)

            else:

                print("You do not have that item")
                choices()



    elif choice.lower() == "health":
        player.giveHealth()
        choices()



    else:
        print("that is not a valid option")
        choices()