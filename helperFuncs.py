from collections import Counter

def sortinv(player):
    counts = dict(Counter(player.inv))
    duplicates = {key:value for key, value in counts.items() if value > 1}
    player.printinv = [""]
    
    for duplicate, count in duplicates.items():
        for item in player.inv:
            if item != duplicate:
                player.printinv.append(item)
            else:
                player.printinv.append(f"{duplicate} x{count}")


    
    unique = list(set(player.printinv))
    player.printinv = unique
















        
