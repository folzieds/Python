import random

# Adding Color to text 
class Bcolors:
    HEADERS="\033[95m"
    OKBLUE="\033[94m"
    OKGREEN="\033[92m"
    WARNING="\033[93m"
    FAIL="\033[91m"
    ENDC="\033[0m"
    BOLD="\033[1m"
    UNDERLINE="\033[4m"

class Person:
    def __init__(self, name,hp, mp, df, attack, magic, items):
        self.max_hp = hp
        self.hp = hp
        self.max_mp = mp
        self.mp = mp
        self.defense = df
        self.high_attack = attack + 10
        self.low_attack = attack - 10
        self.magic = magic
        self.items = items
        self.action = ["Attack", "Magic","Items"]
        self.name=name

    def generate_damage(self):
        return random.randrange(self.low_attack, self.high_attack)

    def take_damage(self, damage):
        self.hp -= damage

        if self.hp < 0:
            self.hp = 0

        return self.hp

    def heal(self, damage):
        self.hp += damage
        if self.hp > self.max_hp:
            self.hp = self.max_hp

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

    def choose_action(self):
        index = 1

        print(f"{Bcolors.OKGREEN}{Bcolors.BOLD}{self.name.upper()}{Bcolors.ENDC}")
        print(f"{Bcolors.OKBLUE}{Bcolors.BOLD}ACTIONS{Bcolors.ENDC}")

        for item in self.action:
            print(f"    {index}. {item}")
            index += 1

    def choose_magic(self):
        index = 1

        print(f"{Bcolors.OKBLUE}{Bcolors.BOLD}MAGIC{Bcolors.ENDC}")

        for spell in self.magic:
            print(f"    {index}. {spell.name} (cost: {spell.cost})")
            index += 1


    def choose_items(self):
        index = 1

        print(f"{Bcolors.OKGREEN}{Bcolors.BOLD}ITEMS{Bcolors.ENDC}")

        for item in self.items:
            print(f"    {index}. {item['item'].name} => cost: {item['item'].prop}, quantity: {item['quantity']}")
            index +=1

    def get_stats(self):
        print("               _________________________          __________")
        print(f"{self.name.upper()}:   {self.hp}/{self.max_hp}|{Bcolors.OKGREEN}█████████████████████████{Bcolors.ENDC}|  {self.mp}/{self.max_mp} |{Bcolors.OKBLUE}██████████{Bcolors.ENDC}|")