import random


def games(player):
    

    print("The games available are:\n50/50")

    choice = input("> ")

    match choice:
        
        case "5050":
            print("Heads or tails?")
            headsOrTchoice = input("> ")

            print("How much are you betting?")

            passed = False

            while passed == False:
                try:
                    bet = int(input(">"))
                    passed = True

                except:
                    print("Please enter an integer")

            headsOrT = random.randint(1,2)
            if (headsOrT == 1 and headsOrTchoice == "heads" or 
                headsOrT == 2 and headsOrTchoice == "tails"):

                print("You won! your bet has been multiplied by 1.5X")
                player.money -= bet
                bet *= 1.5
                player.money += bet
                print(f"Your new balance is {player.money}")
                print("play again, or use leave to return to trader menu")
            
            else:
                print(f"You lost! {bet} has been deducted from your balance")
                player.money -= bet
                print(f"Your new balance is {player.money}")
                print("play again, or use leave to return to trader menu")
        

        case "leave":
            pass
            


            


