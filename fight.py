import random
import json
def fight(player,enemy,enemyhealth):

            weaponInv = []
            for x in player.inv:

                weaponList = ["\nknife", "\nfork", "\nbat", "\ntorch", "\ncrowbar", "\nbranch", "\nshovel"]
                if x in weaponList:
                    weaponInv.append(x)

            if weaponInv == []:
                if enemy == "hard":
                    damageTaken = random.randint(50, 90)
                elif enemy == "medium":
                    damageTaken = random.randint(25, 50)
                elif enemy == "easy":
                    damageTaken = random.randint(2, 25)
                else:
                    print("Fatal error!")
                print(f"You don't have any weapons to attack with, and lost {damageTaken} health")
                player.cHealth -= damageTaken
                print("Pro tip - next time RUN if you don't have any weapons")
                fight()





            else:


                firstTime = True
                while enemyhealth > 0:

                    if player.cHealth == 0 or 0 > player.cHealth:
                        print(f"You ran out of health and died - you had {player.money} pounds")
                        exit()

                    if firstTime == True:
                        print("you have:" + "".join(weaponInv))
                        firstTime = False
                    weaponChoice = input("What weapon do you want to attack the enemy with? > ")
                    print("")









                    if ("\n" + weaponChoice) in weaponInv:

                        if weaponChoice == "torch":
                            didScare = random.randint(1, 100)
                            if didScare < 25:
                                print("You light your torch and scare off the enemy!")
                                player.inv.remove("\ntorch")

                            else:
                                print("The enemy did not care about your torch")

                        else:




                            with open("Json/weapons.json", "r") as f:
                                data = json.load(f)

                                Find = data["weapons"]
                                damageToEnemy = random.choice(Find[weaponChoice])
                                enemyhealth -= damageToEnemy
                                if enemyhealth == 0 or 0 > enemyhealth:
                                    print(
                                        f"You did {damageToEnemy} to the enemy with your {weaponChoice} it now has 0 remaining")
                                else:
                                    print(
                                        f"You did {damageToEnemy} to the enemy with your {weaponChoice}, the enemy now has {enemyhealth} health remaining")



                    elif item not in data["weapons"]:
                        match enemy:
                            case "hard":
                                healthLost = random.randint(50, 90)
                            case "medium":
                                healthLost = random.randint(25, 50)
                            case "easy":
                                healthLost = random.randint(2, 25)
                            case _:
                                print("Fatal error!")

                        print(f"You spent too long looking for a weapon you don't have, and lost {healthLost} health")


                    if enemyhealth > 0:
                        if enemy == "hard":
                            damageTaken = random.randint(50, 90)
                        elif enemy == "medium":
                            damageTaken = random.randint(25, 50)
                        elif enemy == "easy":
                            damageTaken = random.randint(2, 25)
                        else:
                            print("Fatal error!")
                        player.cHealth -= damageTaken
                        print(
                            f"The enemy slashed you and dealt {damageTaken} damage. You now have {player.cHealth} health remaining")
                        print("")

                coinsLooted = random.randint(1, 50)
                print(f"You killed the enemy and ran to another room, and looted £{coinsLooted}")
                player.money += coinsLooted