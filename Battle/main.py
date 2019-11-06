from classes.Game import Person, Bcolors
from classes.Magic import Spell
from classes.Inventory import Item

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
player_item = [portion, high_portion,super_portion,elixir,High_elixir,grenade]

# Instantiate Characters
player = Person(500,65,34,60,player_magic,player_item)
enemy = Person(1200,65,45,25,[],[])

running = True

print(f"{Bcolors.FAIL}{Bcolors.BOLD}THE ENEMY ATTACKS{Bcolors.ENDC}")

while running:
    print("========================")
    player.choose_action()

    choice = int(input("Choose action: ")) - 1
    
    # Attack option
    if choice == 0:
        player_attack_damage = player.generate_damage()
        enemy.take_damage(player_attack_damage)

        print(f"You attacked for {player_attack_damage} points.")

    # Magic option
    elif choice == 1:
        print("=========================")
        player.choose_magic()
        
        magic_choice = int(input("Choose magic: ")) - 1

        #create a variable to store the choice of the magic selected
        spell = player.magic[magic_choice]

        current_mp = player.get_mp()

        # skip reduction of mp if the player's mp is below the cost
        if spell.cost > current_mp:
            print(f"{Bcolors.BOLD}{Bcolors.FAIL}\nNOT ENOUGH MP!!{Bcolors.ENDC}")
            continue
        else:
            player.reduce_mp(spell.cost)

            if spell.type == "white":
                player.heal(spell.damage)
                print(f"\n{Bcolors.OKBLUE}{spell.name} heals for {spell.damage} HP.{Bcolors.ENDC}")

            elif spell.type == "black":
                # Generates the damage and saves it in a variable
                player_magic_damage = spell.generate_damage()
                enemy.take_damage(player_magic_damage)

        print(f"{Bcolors.OKBLUE}{Bcolors.BOLD}{spell.name}  deals {player_magic_damage} points.{Bcolors.ENDC}")

    # Item option
    elif choice == 2:
        print("===============================")
        player.choose_items()

        item_choice = int(input("Choose item: ")) - 1

    # Enemy attacks you
    enemy_choice = 1
    enemy_attack_damage = enemy.generate_damage()
    player.take_damage(enemy_attack_damage)

    print(f"Enemy attacks for {enemy_attack_damage} points.")

    # Print the summary of the attacks for that round
    print("\n--------------------------------")
    print(f"Enemy HP: {Bcolors.FAIL}{enemy.get_hp()}/{enemy.get_max_hp()}{Bcolors.ENDC}\n")

    print(f"Player HP: {Bcolors.OKGREEN}{player.get_hp()}/{player.get_max_hp()}{Bcolors.ENDC}")
    print(f"Player MP: {Bcolors.OKBLUE}{player.get_mp()}/{player.get_max_mp()}{Bcolors.ENDC}\n")

    if enemy.get_hp() == 0:
        print(f"{Bcolors.BOLD}{Bcolors.OKGREEN}YOU WIN!!!{Bcolors.ENDC}")
        running = False
        
    elif player.get_hp() == 0:
        print(f"{Bcolors.BOLD}{Bcolors.FAIL}Your enemy has defeated you. YOU LOST!!!{Bcolors.ENDC}")
        running = False
