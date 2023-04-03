from collections import Counter

def sortinv(player):
    counts = dict(Counter(player.inv))
    duplicates = {key:value for key, value in counts.items() if value > 1}
    
    for duplicate, count in duplicates.items():
        player.printinv.append(f"{duplicate} x{count}")
        
