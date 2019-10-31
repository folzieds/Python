from classes.Game import Person, Bcolors
import random

magic = [{"name": "fire", "damage": 40, "cost": 5},
         {"name": "thunder", "damage": 50, "cost": 10},
         {"name": "blizzard", "damage": 30, "cost": 5}]

player = Person(500,65,34,60,magic)

i = 0
while i<3:
    print(player.generate_spell_damage(random.randint(0,2)))
    i += 1