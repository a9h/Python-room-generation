from collections import Counter

def sortinv(player, inv):

    weaponList = ["\nknife", "\nfork", "\nbat",
    "\ntorch", "\ncrowbar", "\nbranch", "\nshovel", "\nsword", "\nlongsword"]

    



    counts = dict(Counter(inv.inv))
    duplicates = {key:value for key, value in counts.items() if value > 1}
    player.printinv = [""]
    
    with open("Json/itemLists.json", "r") as f:
    



        for duplicate, count in duplicates.items():
            for item in inv.inv:

                if item != duplicate:

                    if item in weaponList:
                        inv.weaponInv.append(item)
                    

                else:
                    if item in weaponList:
                        inv.weaponInv.append(f"{duplicate} x{count}")

                    else:
                        pass
                        



    
    unique = list(set(inv.printinv))
    inv.printinv = unique
















        
