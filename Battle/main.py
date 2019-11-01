from classes.Game import Person, Bcolors


magic = [{"name": "Fire", "damage": 100, "cost": 5},
         {"name": "Thunder", "damage": 150, "cost": 10},
         {"name": "Blizzard", "damage": 100, "cost": 5}]


player = Person(500,65,34,60,magic)
enemy = Person(1200,65,45,25,magic)

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

        #get the details of the spell
        spell_name = player.get_spell_name(magic_choice)
        spell_cost = player.get_spell_mp_cost(magic_choice)

        current_mp = player.get_mp()

        # skip reduction of mp if the player's mp is below the cost
        if spell_cost > current_mp:
            print(f"{Bcolors.BOLD}{Bcolors.FAIL}\nNOT ENOUGH MP!!{Bcolors.ENDC}")
            continue
        else:
            player.reduce_mp(spell_cost)
        
            player_magic_damage = player.generate_spell_damage(magic_choice)
            enemy.take_damage(player_magic_damage)

        print(f"{Bcolors.OKBLUE}{Bcolors.BOLD}{spell_name}  deals {player_magic_damage} points.{Bcolors.ENDC}")

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
