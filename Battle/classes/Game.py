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
    def __init__(self, name,hp, mp, df, attack, magic, items,character):
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
        self.character=character

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

    def attack(self, enemies):

        #generates damage for the player
        player_attack_damage = self.generate_damage()

        if self.character == "player":
            target = self.choose_target(enemies)
        elif self.character == "enemy":
            target = random.randrange(0, len(enemies))

        enemies[target].take_damage(player_attack_damage)

        print(f"{Bcolors.OKYELLOW}{self.name} attacked {enemies[target].name} for {player_attack_damage} points.{Bcolors.ENDC}")

        if enemies[target].get_hp() == 0:
            print(f"{enemies[target].name} has died")
            del enemies[target]

    def magic_attack(self, enemies):

        magic_choice = 0
        if self.character == "player":
            self.choose_magic()
            magic_choice = int(input("Choose magic: ")) - 1
        elif self.character == "enemy":
            magic_choice = random.randrange(0,len(self.magic))

        # create a variable to store the choice of the magic selected
        spell = self.magic[magic_choice]

        current_mp = self.get_mp()

        if magic_choice == -1:
            pass

        # skip reduction of mp if the player's mp is below the cost
        if spell.cost > current_mp:
            print(f"{Bcolors.BOLD}{Bcolors.FAIL}\nNOT ENOUGH MP!!{Bcolors.ENDC}")
            return
        else:
            self.reduce_mp(spell.cost)

            if spell.spell_type == "white":
                self.heal(spell.damage)
                print(f"\n{Bcolors.OKBLUE}{spell.name} heals for {spell.damage} HP.{Bcolors.ENDC}")

            elif spell.spell_type == "black":
                # Generates the damage and saves it in a variable
                player_magic_damage = spell.generate_damage()

                enemy = self.choose_target(enemies)
                enemies[enemy].take_damage(player_magic_damage)

                print(
                    f"{Bcolors.OKBLUE}{Bcolors.BOLD}{spell.name}  deals {player_magic_damage} points to {enemies[enemy].name}.{Bcolors.ENDC}")

                if enemies[enemy].get_hp() == 0:
                    print(f"{enemies[enemy].name} has died")
                    del enemies[enemy]

    def use_item(self, enemies, players):

        item_choice = 0
        if self.character == "player":
            self.choose_items()

            item_choice = int(input("Choose item: ")) - 1

        elif self.character == "enemy":
            item_choice = random.randrange(0, len(self.items))

        if item_choice == -1:
            pass

        item_chosen = self.items[item_choice]["item"]

        if self.items[item_choice]["quantity"] == 0:
            print(f"{Bcolors.FAIL}\nNone left...{Bcolors.ENDC}")
            pass

        self.items[item_choice]["quantity"] -= 1

        if item_chosen.item_type == "portion":
            self.heal(item_chosen.prop)

            print(f"\n{Bcolors.OKGREEN}{Bcolors.BOLD}{item_chosen.name} heals for {item_chosen.prop} HP{Bcolors.ENDC}")

        elif item_chosen.item_type == "elixir":
            if item_chosen.name == "Mega Elixir":
                for i in players:
                    i.hp = i.max_hp
                    i.mp = i.max_mp
            else:
                self.hp = self.max_hp
                self.mp = self.max_mp

            print(f"\n{Bcolors.OKBLUE}{item_chosen.name} fully restores HP/MP{Bcolors.ENDC}")

        elif item_chosen.item_type == "attack":
            enemy = self.choose_target(enemies)
            enemies[enemy].take_damage(item_chosen.prop)

            print(
                f"{Bcolors.FAIL}{item_chosen.name} deals {item_chosen.prop} points of damage to {enemies[enemy].name}{Bcolors.ENDC}")

            if enemies[enemy].get_hp() == 0:
                print(f"{enemies[enemy].name} has died")
                del enemies[enemy]