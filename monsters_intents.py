import attack_system

#patterns
def patpat(name, pattern: int, atk: int):
    if pattern == 1:
        print(f"The {name} intends to attack for {atk} damage!") #light

    if pattern == 2:
        this = atk * 2
        print(f"The {name} intends to deal double ({this}) damage!") #heavy


#attacks

def helit(name, hp, atk, defe):
    hp = attack_system.damage_light(name, hp, atk, defe) #light
    return hp

def hehit(name, hp, atk, defe):
    hp = attack_system.damage_heavy(name, hp, atk, defe) #heavy
    return hp

