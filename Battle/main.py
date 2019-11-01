from classes.Game import Person, Bcolors
from classes.Magic import Spell

# Black Magic
fire = Spell("Fire", 5, 100, "black")
thunder = Spell("Thunder", 10, 150, "black")
blizzard = Spell("Blizzard", 5, 100, "black")
meteor = Spell("Meteor", 15, 200, "black")
quake = Spell("Quake", 13, 170, "black")

# White Magic
cure = Spell("Cure", 15, 150, "white")
cura = Spell("Cura", 20, 250, "white")

# Instantiate Characters
player = Person(500,65,34,60,[fire, thunder, blizzard, meteor, cure, cura])
enemy = Person(1200,65,45,25,[])

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

            # Generates the damage and saves it in a variable
            player_magic_damage = spell.generate_damage()
            enemy.take_damage(player_magic_damage)

        print(f"{Bcolors.OKBLUE}{Bcolors.BOLD}{spell.name}  deals {player_magic_damage} points.{Bcolors.ENDC}")

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
