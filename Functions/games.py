import random


def games(player):
    

    print("The games available are:\n50/50,\nH/L")

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
                choice1 = input("> ")

                match choice1:

                    case "play", "again":
                        games(player=player)
                    case "return":
                        pass

                


            
            else:
                print(f"You lost! {bet} has been deducted from your balance")
                player.money -= bet
                print(f"Your new balance is {player.money}")
                print("play again, or use leave to return to trader menu")

                choice2 = input("> ")
                
                match choice2:

                    case "play", "again":
                        games(player=player)
                    case "return":
                        pass
        

        case "leave":
            pass

        case "h/l":
            higherOrLower(player1=player)
            

def higherOrLower(player1):
    
            


    number = random.randrange(1, 100)
    hint_def = random.randrange(1, 100)

    if number > 50:
        hint = random.randrange(50, 100)

    elif number < 50:
        hint = random.randrange(1, 50)

    passed = False

    while passed == False:
        try:
            print("please enter your bet")
            bet = int(input(">"))
            passed = True

        except:
            print("Please enter an integer")
            
    player1.money = player1.money - bet

    print(f"High-Low game A hidden number between 1 and 100 has been chosen.\n The hint is {hint}")

    guess = input("please guess higher or lower: >")
        


    if guess == "higher" or guess == "lower":
            if guess == "higher" and hint < number:
                print(f"Correct! the number was {number}")
                toAdd = float(bet) * 1.5
                player1.money = player1.money + toAdd
            elif guess.content == "lower" and hint > number:

                print(f"correct! the number was {number}")
                toAdd = float(bet) * 1.5
                player1.money = player1.money + toAdd
            elif guess.content == "lower" and number > hint or guess.content == "high" and number < hint:
                print(f"WRONG! the number was {number}")
                
            elif guess == number:
                print("SPOT ON! Your bet was multiplied by 8x")
                toAdd = float(bet) * 8
                player1.money = player1.money + toAdd


    else:
        print(f"please enter higher or lower!")
        higherOrLower(player1=player1)


    games(player=player1)