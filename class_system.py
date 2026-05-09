#At least 3 classes
    #Requires misdemeaning names for each class, because that's funny

#Different stats per class

#Different skills per classes (optional)?

#Different inventory depending on class? (optional)
    #need to figure out how to edit stats depending on items in inventory
    #need to figure out how to induce healing and then remove that item from inventory
        #reminder, dictionaries can't have duplicates

def decide(player):
    while True:
        print("Decide your class")
        print(" 1. Meat Shield\n  -Trudging, simple beast with no survival instincts\n  -high defense, low attack")
        print(" 2. Poor Brigand\n  -Frail thief armed with nothing but what it's stolen\n  -low defense, high attack")
        print(" 3. Macabre\n  -A creature capable of confusing magics, most harming itself\n  -mid defense, mid attack")
        cls = int(input("(1,2,3)>"))
        match cls:
            case 1:
                player = "Meat Shield"
                break
            case 2:
                player = "Poor Brigand"
                break
            case 3:
                player = "Macabre"
                break
            case _:
                print("INVALID")
    return player

#class ideas (OPTIONAL):

    #Meat Shield
        #A trudging, simple beast with no survival instincts
        #Tank character - high defense, low attack
        #Less money at the start than the brigand
        #Skills based on healing and defense

    #Poor Brigand
        #A frail thief armed with nothing but what it's stolen
        #Offensive character - low defense, high attack
        #More money at the start than other characters
        #Skills based on boosting attack

    #Macabre
        #A creature capable of confusing magics, most harming itself
        #Wild card character - mid defense, mid attack
        #No money at the start
        #Skill cause miscellaneous effects, at the cost of health
