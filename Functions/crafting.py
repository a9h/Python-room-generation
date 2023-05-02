import os
from pystyle import Write, Colors
import json
import time
class craftables:
        def __init__(self,completeRecipies,craftInv) -> None:
                self.completeRecipies = completeRecipies
                self.craftInv = craftInv



        


craftables = craftables([], [])






def getRecepies(ingredients):




                




        with open ("Json/recipies.json", "r") as r:
                data = json.load(r)
                for thing in data:
                        scrapcount = 0
                        ironcount = 0
                        for b in data[thing]:
                                if b == "\nscrapmetal":
                                        scrapcount += 1
                                elif b == "\niron":
                                        ironcount += 1

                        if scrapcount <= ingredients.metal and ironcount <= ingredients.iron:
                                craftables.completeRecipies.append("".join(thing))
                        else:
                                pass
                




                

                

                        

                        

        

        





                        
                                
def make(inv,ingredients):
        print("available recipies: \n".join(craftables.completeRecipies))


        if craftables.completeRecipies == []:
                print("There is nothing you can craft!")
                
        else:
                with open ("Json/recipies.json", "r") as r:
                        data = json.load(r)
                        choice = input("> ")
                        for thing in data:
                                
                                if thing == choice:
                                        scrapcount = 0
                                        ironcount = 0
                                        for b in data[thing]:
                                                if b == "\nscrapmetal":
                                                        scrapcount += 1
                                                elif b == "\niron":
                                                        ironcount += 1
                                        if scrapcount <= ingredients.metal and ironcount <= ingredients.iron:
                                                        print(f"-- Crafted {thing} --")
                                                        print(f"It used {scrapcount} metal and {ironcount} iron")


                                                        input()
                                                        inv.inv.append(f"\n{thing}")

                                                        ingredients.metal =- scrapcount 
                                                        ingredients.iron =- ironcount

                                                        
                                                        for c in data[thing]:
                                                                if c == "\nscrapmetal":
                                                                        inv.inv.remove("\nscrapmetal")
                                                                elif c == "\niron":
                                                                        inv.inv.remove("\niron")

                                                        
                                                        crafting(inv=inv,ingredients=ingredients)
                                        else:
                                                print("you do not have the correct ingredients!")
                                                input()
                                                crafting(inv=inv,ingredients=ingredients)

                                else:
                                        pass

                                        
                                                




                                
        


    
    






def crafting(inv,ingredients):
        os.system("clear")
        Write.Print("""
    ╔════════════════════════════════════════════╗   
    ║    ╔═╗  ╦═╗  ╔═╗  ╔═╗  ╔╦╗  ╦  ╔╗╔  ╔═╗    ║  
    ║    ║    ╠╦╝  ╠═╣  ╠╣    ║   ║  ║║║  ║ ╦    ║
    ║    ╚═╝  ╩╚═  ╩ ╩  ╚     ╩   ╩  ╝╚╝  ╚═╝    ║
    ╚════════════════════════════════════════════╝
            Use 'make' to start crafting                                                    
            ═══════════════════════════╝                           
""", Colors.white, interval=0.005)


        getRecepies(ingredients=ingredients)

       
        choice = input(">")

        match choice:
                case "make":
                        make(inv=inv,ingredients=ingredients)
                case "exit": 
                        os.system("clear")
                case _:
                        crafting(inv=inv,ingredients=ingredients)
        
    





    