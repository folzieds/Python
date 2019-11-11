import random

class Spell:
    def __init__(self, name, cost, damage, spell_type):
        self.name = name
        self.cost = cost
        self.damage = damage
        self.spell_type = spell_type

    def generate_damage(self):
        low = self.damage - 15
        high = self.damage + 15
        return random.randrange(low,high)