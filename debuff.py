player = { #3
    
    "name": "YOU",
    # "name": name,
    "atk" : 100,
    "hp"  : 1000,
    "hp_max"  : 1000,
    "mp"  : 100,
    "mp_max"  : 100,
    "def" : 1,
    "cls" : "THIS SHOULDN'T APPEAR",
    "poison" : 10
    
}

def poison(player:dict):
    player['hp'] -= 5
    player['poison'] -= 1

    print(f"Poisoned(-5HP per-turn): {player['poison']} turns remaining")

    return player