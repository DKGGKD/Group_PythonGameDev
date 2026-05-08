#for testing code
from monsters import spawn_monster
from monsters import monsters


player = {
    "name": "BLANK",
    "atk": 3,
    "hp" : 1,
    "def" : 5
}

#CHECKING PLAYER STATS requires: from monsters import spawn_monster, monsters
# def check():
#     print("--------------------------")
#     print(f"Name: {player["name"]}\nAttack: {player["atk"]}\nHP: {player["hp"]}\nDefense: {player["def"]}")
#     print(f"\nOpponent: {monst_name}\nAttack: {monst_atk}\nHP: {monst_hp}\nDefense: {monst_def}")
#     print("--------------------------")


#HEAL HP
# def heal():
#     player["hp"] += 15
#     if player["hp"] > 20:
#         something = player["hp"] - 20
#         player["hp"] -= something
#     print(f"You healed back up to {player["hp"]} hp!")

#DAMAGE CALC
# boost = 30
# def damage_calc(power): #calcs damage
#     damage = power + boost
#     damage -= monst_def
#     return damage

# def damage_monster(hp: int, atk: int): #damages monster
#     atk = damage_calc(atk)
#     damage = hp - atk
#     print(f"You attacked the monster for {atk} damage")
#     return damage

# monst_name, monst_atk, monst_hp, monst_def = spawn_monster()
# monst_hp = damage_monster(monst_hp, player["atk"])