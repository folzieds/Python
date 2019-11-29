import random

# Adding Color to text 
class Bcolors:
    HEADERS="\033[95m"
    OKBLUE="\033[94m"
    OKGREEN="\033[92m"
    OKYELLOW = "\033[93m"
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

    def choose_target(self, enemies):
        index  = 1

        print(f"{Bcolors.FAIL}{Bcolors.BOLD}TARGET{Bcolors.ENDC}")

        for i  in enemies:
            print(f"    {index}. {i.name}")
            index += 1

        return int(input("Choose Target: ")) - 1


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

    def get_enemy_stats(self):
        hp_bar =""
        bar = "█"

        LENGTH_OF_HP_BAR = 50
        BAR_COLOR = Bcolors.FAIL

        hp_status = int(round((self.hp / self.max_hp) * LENGTH_OF_HP_BAR))

        while hp_status > 0:
            hp_bar += bar
            hp_status -=1
        while len(hp_bar) < LENGTH_OF_HP_BAR:
            hp_bar += " "

        if self.hp < (self.max_hp / 4):
            BAR_COLOR = Bcolors.OKYELLOW

        print("                 __________________________________________________")
        print(f"{self.name.upper()}:   {self.hp:4}/{self.max_hp:4}|{BAR_COLOR}{hp_bar}{Bcolors.ENDC}|")

    def get_stats(self):
        hp_bar =""
        mp_bar = ""
        bar = "█"

        LENGTH_OF_HP_BAR = 25
        LENGTH_OF_MP_BAR = 10
        BAR_COLOR = Bcolors.OKGREEN

        hp_status = int(round((self.hp/self.max_hp) * LENGTH_OF_HP_BAR))
        mp_status = int(round((self.mp/self.max_mp) * LENGTH_OF_MP_BAR))

        while hp_status > 0:
            hp_bar += bar
            hp_status -=1
        while len(hp_bar) < LENGTH_OF_HP_BAR:
            hp_bar += " "

        while mp_status > 0:
            mp_bar += bar
            mp_status -=1

        while len(mp_bar) < LENGTH_OF_MP_BAR:
            mp_bar += " "

        if self.hp < (self.max_hp / 4):
            BAR_COLOR = Bcolors.FAIL


        print("               _________________________          __________")
        print(f"{self.name.upper()}:   {self.hp:3}/{self.max_hp:3}|{BAR_COLOR}{hp_bar}{Bcolors.ENDC}|  {self.mp:2}/{self.max_mp:2} |{Bcolors.OKBLUE}{mp_bar}{Bcolors.ENDC}|")