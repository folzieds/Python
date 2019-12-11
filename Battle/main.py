from classes.Game import Person, Bcolors
from classes.Magic import Spell
from classes.Inventory import Item
import random
import simplejson

# Black Magic
fire = Spell("Fire", 5, 100, "black")
thunder = Spell("Thunder", 10, 150, "black")
blizzard = Spell("Blizzard", 5, 100, "black")
meteor = Spell("Meteor", 15, 200, "black")
quake = Spell("Quake", 13, 170, "black")

# White Magic
cure = Spell("Cure", 15, 150, "white")
cura = Spell("Cura", 20, 250, "white")


# Items
portion = Item("Portion","portion","Heals 50 Hp",50)
high_portion = Item("High Portion","portion","Heals 100 Hp",100)
super_portion = Item("Super Portion","portion","Heals 500 Hp",500)
elixir = Item("Elixir", "elixir", "Heals one characters Hp/Mp to maximum", 9999)
High_elixir = Item("Mega Elixir","elixir","Fully restores Hp/Mp of party", 9999)

# attack items
grenade = Item("Grenade","attack", "Deals 500 damage", 500)

player_magic = [fire, thunder, blizzard, meteor, cure, cura]
player_item = [{"item":portion,"quantity": 15}, {"item":high_portion,"quantity": 15},{"item":super_portion,"quantity": 5},
               {"item":elixir,"quantity": 5},{"item":High_elixir,"quantity": 2},{"item":grenade,"quantity": 5}]

enemy_magic = [fire, thunder, blizzard, meteor, cure, cura]
enemy_item = [{"item":portion,"quantity": 15}, {"item":high_portion,"quantity": 15},{"item":super_portion,"quantity": 5},
               {"item":elixir,"quantity": 5},{"item":High_elixir,"quantity": 2},{"item":grenade,"quantity": 5}]

# Instantiate Characters
player1 = Person("ade",500,65,34,60,player_magic,player_item,"player")
player2 = Person("ore",500,65,34,60,player_magic,player_item,"player")
player3 = Person("uju",500,65,34,60,player_magic,player_item,"player")

players = [player1, player2, player3]

# initiate enemies
enemy1 = Person("Imp", 400,30,20,30,enemy_magic,enemy_item,"enemy")
enemy2 = Person("Van",1200,65,45,125,enemy_magic,enemy_item,"enemy")
enemy3 = Person("Imp", 400,30,20,30,enemy_magic,enemy_item,"enemy")

enemies = [enemy1, enemy2, enemy3]

running = True

print(f"{Bcolors.FAIL}{Bcolors.BOLD}THE ENEMY ATTACKS{Bcolors.ENDC}")

while running:

    print("========================", end="\n")
    print("NAME           HP                                 MP")

    for player in players:
        player.get_stats()

    for enemy in enemies:
        enemy.get_enemy_stats()

    for player in players:
        print("========================",end="\n\n")
        player.choose_action()

        try:

            choice = int(input("Choose action: ")) - 1

            # Attack option
            if choice == 0:
                player.attack(enemies)

            # Magic option
            elif choice == 1:
                print("=========================")
                player.magic_attack(enemies)

            # Item option
            elif choice == 2:
                print("===============================")
                player.use_item(enemies,players)

        except Exception as error:
            print(f"{Bcolors.FAIL}{Bcolors.BOLD}\n....INVALID INPUT....{Bcolors.ENDC}")
            print(f"{error}")
            continue

        #check if player has won
        if len(enemies) == 0:
            print(f"{Bcolors.BOLD}{Bcolors.OKGREEN}YOU WIN!!!{Bcolors.ENDC}")
            running = False
            break

    # Enemy attack phase
    for enemy in enemies:
        enemy_choice = random.randrange(0,3)

        # Enemy attack option
        if enemy_choice == 0:
            enemy.attack(players)

        elif enemy_choice == 1:
            enemy.magic_attack(players)

        elif enemy_choice == 2:
            enemy.use_item(players,enemies)

        #  Check if enemy has won
        if len(players) == 0:
            print(f"{Bcolors.BOLD}{Bcolors.FAIL}Your enemy has defeated you. YOU LOST!!!{Bcolors.ENDC}")
            running = False



#todo: when you go back up one level it should actually go back up one level and not skip to the next person
#todo: handle when the user enters a wrong input
