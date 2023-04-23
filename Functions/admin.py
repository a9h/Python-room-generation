def admin(player,inv):
    print("stat editor:")
    code = input("> ")

    match code:
        case "inv.remove":

            item=input("item > ")
            inv.inv.remove(item)

        
            
