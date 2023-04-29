import os
from pystyle import Write, Colors
import json

class craftables:
        def __init__(self,completeRecipies) -> None:
                self.completeRecipies = completeRecipies


craftables = craftables([])







        





"""
def recipies(inv):
        with open ("Json/recipies.json", "r") as f:
                data = json.load(f)
                for recipie in data:
                        print(recipie)
                        counter1 = 0
                        counter2 = 0
                        for item in recipie:
                                print(item)
                                counter1 = counter1 + 1

                                for x in inv.craftingInv:
                                        if x == ("\n"+item):
                                                counter2 = counter2 +1
                                        else:
                                                pass

                        if counter1 == counter2:
                                craftables.completeRecipies.append(item)
                        else:
                                 pass
                        
                print(f"available recipies: {craftables.completeRecipies}")
                input()
"""
                        
                                

                        
                                
        


    
    






def crafting(player, inv):
        os.system("clear")
        Write.Print("""
    ╔════════════════════════════════════════════╗   
    ║    ╔═╗  ╦═╗  ╔═╗  ╔═╗  ╔╦╗  ╦  ╔╗╔  ╔═╗    ║  
    ║    ║    ╠╦╝  ╠═╣  ╠╣    ║   ║  ║║║  ║ ╦    ║
    ║    ╚═╝  ╩╚═  ╩ ╩  ╚     ╩   ╩  ╝╚╝  ╚═╝    ║
    ╚════════════════════════════════════════════╝
                                                                
            ════════════════════════╝                           
""", Colors.white, interval=0.005)

        input()
        
    





    