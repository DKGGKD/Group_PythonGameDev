from random import choice
monsters = [
    #0
    ("goblin", 5, 10),
    #1
    ("slime", 3, 5)
]

def spawn_monster():
    
    monster = choice(monsters)
    return monster