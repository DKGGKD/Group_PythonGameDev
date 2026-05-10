#for testing code
# from monsters import spawn_monster
import textstuff, attack_system
from monsters import spawn_monster

# from monsters_intents import something
# import random, attack_system, math


# player = {
#     "name": "BLANK",
#     "atk": 3,
#     "hp" : 5,
#     "hp_max" : 10,
#     "def" : 5,
#     "mp" : 20,
#     "mp_max" : 20
# }
# extra = 0

player = { #3
    
    "name": "YOU",
    # "name": name,
    "atk" : 1,
    "hp"  : 100,
    "hp_max"  : 100,
    "mp"  : 100,
    "mp_max"  : 100,
    "def" : 1,
    "cls" : "THIS SHOULDN'T APPEAR"
    
}
# print(f"\n{player['hp']}")

# monster = spawn_monster()
# print(monster)

# player["hp"] = attack_system.damage_light(monster, player)

# print(f"\n{player['hp']}")
print(f"{player['hp']}")
damage = attack_system.damage_player(player['hp'], 25, player['def'])
print(f"this is damage {damage}")
print(f"this is hp {player['hp']}")
player['hp'] -= damage
print(f"this is after {player['hp']}")

# import skill_system, textstuff
# from monsters import spawn_monster
# player = { #3
    
#     "name": "YOU", #for testing
#     #"name": name,
#     "atk" : 10,
#     "hp"  : 1,
#     "hp_max"  : 100,
#     "mp"  : 20,
#     "mp_max"  : 20,
#     "def" : 1,
#     "cls" : "THIS SHOULDN'T APPEAR"
    
# }
# extra = 0

# monst_name, monst_atk, monst_hp, monst_def = spawn_monster()
# textstuff.spawn(player["name"], monst_name)

# status = monst_name, monst_atk, monst_hp, monst_def

# player["mp"], player["hp"], extra = skill_system.skill_menu(player, extra, status)

# print(f"MP: {player["mp"]}\nHP:{player["hp"]}\nExtra:{extra}")




# extra = 0

#CHECKING PLAYER STATS requires: from monsters import spawn_monster, monsters

# import skill_system
# from game_group import player
# from monsters import monsters, spawn_monster

# def check(player:dict, monster:tuple):
#     print("--- STATS ---")
#     print(f"*{player['name']}*\nAttack: {player['atk']}\nHP: {player['hp']}\nDefense: {player['def']}")
#     print(f"\n*{monster['monst_name']}*\nAttack: {monster['monst_atk']}\nHP: {monster['monst_hp']}\nDefense: {monster['monst_def']}")
#     print("--- STATS ---")

# check(player, spawn_monster)


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

#BETTER ATTACK SYSTEM
# def damage_player(hp, atk, defe):
#     atk -= defe
#     damage = hp - atk
#     if atk <= 0:
#         atk = 0
#     print(f"The monster deals {atk} damage!")
#     print(f"------------------------------")
#     return damage

# def damage_heavy(hp, atk, defe):
#     atk += 30
#     damage = damage_player(hp, atk, defe) #WOOOOOOAH YOU CAN LITERALLY JUST PUT IT HERE
#     print(f"The monster is exhausted...\n")
#     return damage

# monst_name, monst_atk, monst_hp, monst_def = spawn_monster()

# tired = 0

# while True: #oh no this looping, WHYYYYYYYY
#     if tired == 1: #if the monster is tired
#         print("The monster is tired...") #skip everything else
#     else:
#         pattern = random.randrange(3, 4) #pick a num 1-3, never plays if tired
#         intend(pattern)

#     print(monst_hp)
#     action = input("Please select your action\n>")

#     if action == "1": 

#         monster_hp = attack_system.damage_monster(monst_hp, player["atk"], monst_def, extra) #5

#         if tired == 1: #AAAAAAAAAAAAAAAAAAAAAAA SO MANY NESTED-IFS
#             print("The monster rests this turn!")
#             print(f"------------------------------")
#             tired = 0 #not tired anymore
#         else:
#             if monster_hp <= 0:
#                 print(f"------------------------------")
#                 print(f"You have defeated the monster!!!")
#                 print(f"------------------------------")
#                 break
#             else:
#                 if pattern == 1:
#                     damage_player(player["hp"], monst_atk, player["def"])
#                 elif pattern == 2:
#                     damage_heavy(player["hp"], monst_atk, player["def"])
#                     tired = 1 #be tired

# import battle

# player = { #3
#     "atk": 3,
#     "hp" : 100,
#     "def" : 0
# }

# while True:
#     iny = input("choose:")

#     if iny == "1":
#         battle.battleloop(player["hp"], player["atk"], player["def"])
#     else:
#         break