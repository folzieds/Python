import random

class Bcolors:
    HEADERS="\033[95n"
    OKBLUE="\033[94n"
    OKGREEN="\033[92n"
    WARNING="\033[93n"
    FAIL="\033[91n"
    ENDC="\033[0n"
    BOLD="\033[1n"
    UNDERLINE="\033[4n"

class Person:
    def __init__(self, hp, mp, df, attack, magic):
        self.max_hp = hp
        self.hp = hp
        self.max_mp = mp
        self.mp = mp
        self.defense = df
        self.magic = magic
        self.high_attack = attack + 10
        self.low_attack = attack - 10
        self.magic = magic
        self.action = ["Attack", "Magic"]

    def generate_damage(self):
        return random.randrange(self.low_attack, self.high_attack)

    def generate_spell_damage(self,index):
        magic_low = self.magic[index]["damage"] - 5
        magic_high = self.magic[index]["damage"] + 5
        
        return random.randint(magic_low,magic_high)

    def take_damage(self, damage):
        self.hp -= damage

        if self.hp < 0:
            self.hp = 0

        return self.hp

    def get_hp(self):
        return self.hp

    def get_max_hp(self):
        return self.max_hp

    def get_mp(self):
        return self.mp

    def get_max_mp(self):
        return self.max_mp

    def reduce_mp(self, cost):
        self.mp -= cost

    def get_spell_name(self,index):
        return self.magic[index]["name"]

    def get_spell_mp_cost(self, index):
        return self.magic[index]["cost"]

    def choose_action(self):
        index = 1

        print("Actions")

        for item in self.action:
            print(f"{index}: {item}")
            index += 1

    def choose_magic(self):
        index = 1

        print("Magic")

        for spell in self.magic:
            print(f"{index}: {spell['name']} cost: {spell['cost']}")
