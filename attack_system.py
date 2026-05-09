#possible additions:
    #attack boost calculations (DONE)
    #make calculations depending on defense (DONE)
        #possibly make 3rd variable called 'final_damage'?
        #+'final_damage' through boosts;
        #-'final_damage' from monster_defense

def damage_calc(power, block, boost): #calcs damage
    damage = power + boost
    damage -= block
    return damage

def damage_monster(name, hp: int, atk: int, defe: int, extra: int): #damages monster
    atk = damage_calc(atk, defe, extra)
    if atk <= 0:
        atk = 0
    damage = hp - atk
    print(f"With a defense of {defe}...")
    print(f"{name} attacks the monster for {atk} damage")
    return damage
    


def damage_player(hp, atk, defe):
    damage = atk - defe
    if damage <= 0:
        damage = 0
    return hp - damage

def damage_light(name, hp, atk, defe):
    damage = damage_player(hp, atk, defe)
    output = hp - damage
    if output < 0:
        output = 0
    print(f"With a defense of {defe}...")
    print(f"The {name} deals {output} damage!")
    return damage

def damage_heavy(name, hp, atk, defe):
    fd = atk * 2
    damage = damage_player(hp, fd, defe) #WOOOOOOAH YOU CAN LITERALLY JUST PUT IT HERE
    output = hp - damage
    if output < 0:
        output = 0
    print(f"With a defense of {defe}...")
    print(f"The {name} exhausts itself for {output} damage!")
    return damage