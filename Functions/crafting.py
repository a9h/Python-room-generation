import os
from pystyle import Write, Colors


def crafting(player, inv):
    os.system("clear")
    Write.Print("""
╔════════════════════════════════════════════╗   
║                                            ║
║    ╔═╗  ╦═╗  ╔═╗  ╔═╗  ╔╦╗  ╦  ╔╗╔  ╔═╗    ║  
║    ║    ╠╦╝  ╠═╣  ╠╣    ║   ║  ║║║  ║ ╦    ║
║    ╚═╝  ╩╚═  ╩ ╩  ╚     ╩   ╩  ╝╚╝  ╚═╝    ║
║                                            ║
╚════════════════════════════════════════════╝
                                                            
          ════════════════════════╝                           
    """, Colors.white, interval=0.005)

crafting(player=1)
    