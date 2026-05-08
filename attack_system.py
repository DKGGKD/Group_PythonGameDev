    
def damage_monster(hp: int, atk: int):
    
    damage = hp - atk
    print(f"You attacked the monster for {atk} damage")
    return damage
    
def damage_player(hp, atk):
    
    damage = hp - atk
    print(f"The monster counter attacked for {atk} damage!")
    return damage

if __name__ == "__main__":
    
    print("I will always appear")
    print("I will just appear when ran directly")
    #monster_attack()