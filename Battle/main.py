from classes.Game import Person, Bcolors
from classes.Magic import Spell
from classes.Inventory import Item
import random

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

# Instantiate Characters
player1 = Person("ade",500,65,34,60,player_magic,player_item)
player2 = Person("ore",500,65,34,60,player_magic,player_item)
player3 = Person("uju",500,65,34,60,player_magic,player_item)

players = [player1, player2, player3]

# initiate enemies
enemy1 = Person("Imp", 400,30,20,30,[],[])
enemy2 = Person("Van",1200,65,45,125,[],[])
enemy3 = Person("Imp", 400,30,20,30,[],[])

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
                player_attack_damage = player.generate_damage()

                enemy = player.choose_target(enemies)
                enemies[enemy].take_damage(player_attack_damage)

                print(f"{Bcolors.OKYELLOW}You attacked {enemies[enemy].name} for {player_attack_damage} points.{Bcolors.ENDC}")

                if enemies[enemy].get_hp() == 0:
                    print(f"{enemies[enemy].name} has died")
                    del enemies[enemy]


            # Magic option
            elif choice == 1:
                print("=========================")
                player.choose_magic()

                magic_choice = int(input("Choose magic: ")) - 1

                #create a variable to store the choice of the magic selected
                spell = player.magic[magic_choice]

                current_mp = player.get_mp()

                if magic_choice == -1:
                    continue

                # skip reduction of mp if the player's mp is below the cost
                if spell.cost > current_mp:
                    print(f"{Bcolors.BOLD}{Bcolors.FAIL}\nNOT ENOUGH MP!!{Bcolors.ENDC}")
                    continue
                else:
                    player.reduce_mp(spell.cost)

                    if spell.spell_type == "white":
                        player.heal(spell.damage)
                        print(f"\n{Bcolors.OKBLUE}{spell.name} heals for {spell.damage} HP.{Bcolors.ENDC}")

                    elif spell.spell_type == "black":
                        # Generates the damage and saves it in a variable
                        player_magic_damage = spell.generate_damage()

                        enemy = player.choose_target(enemies)
                        enemies[enemy].take_damage(player_magic_damage)

                        print(f"{Bcolors.OKBLUE}{Bcolors.BOLD}{spell.name}  deals {player_magic_damage} points to {enemies[enemy].name}.{Bcolors.ENDC}")

                        if enemies[enemy].get_hp() == 0:
                            print(f"{enemies[enemy].name} has died")
                            del enemies[enemy]

            # Item option
            elif choice == 2:
                print("===============================")
                player.choose_items()

                item_choice = int(input("Choose item: ")) - 1

                if item_choice == -1:
                    continue

                item_chosen = player.items[item_choice]["item"]

                if player.items[item_choice]["quantity"] == 0:
                    print(f"{Bcolors.FAIL}\nNone left...{Bcolors.ENDC}")
                    continue

                player.items[item_choice]["quantity"] -= 1

                if item_chosen.item_type == "portion":
                    player.heal(item_chosen.prop)

                    print(f"\n{Bcolors.OKGREEN}{Bcolors.BOLD}{item_chosen.name} heals for {item_chosen.prop} HP{Bcolors.ENDC}")

                elif item_chosen.item_type == "elixir":
                    if item_chosen.name == "Mega Elixir":
                        for i in players:
                            i.hp = i.max_hp
                            i.mp = i.max_mp
                    else:
                        player.hp = player.max_hp
                        player.mp = player.max_mp

                    print(f"\n{Bcolors.OKBLUE}{item_chosen.name} fully restores HP/MP{Bcolors.ENDC}")

                elif item_chosen.item_type == "attack":
                    enemy = player.choose_target(enemies)
                    enemies[enemy].take_damage(item_chosen.prop)

                    print(f"{Bcolors.FAIL}{item_chosen.name} deals {item_chosen.prop} points of damage to {enemies[enemy].name}{Bcolors.ENDC}")

                    if enemies[enemy].get_hp() == 0:
                        print(f"{enemies[enemy].name} has died")
                        del enemies[enemy]

        except Exception as error:
            print(f"{Bcolors.FAIL}{Bcolors.BOLD}\n....INVALID INPUT....{Bcolors.ENDC}")
            print(f"{error}")
            continue

    #check if player has won
    if len(enemies) == 0:
        print(f"{Bcolors.BOLD}{Bcolors.OKGREEN}YOU WIN!!!{Bcolors.ENDC}")
        running = False

    # Enemy attack phase
    for enemy in enemies:
        enemy_choice = random.randrange(0,3)

        if len(enemies) != 0:
            enemy_attack_damage = enemies[0].generate_damage()
            target = random.randrange(0,len(players))
            players[target].take_damage(enemy_attack_damage)
            print(f"{Bcolors.OKYELLOW}Enemy attacks {players[target].name} for {enemy_attack_damage} points.{Bcolors.ENDC}")

        if players[target].get_hp() == 0:
            print(f"{players[target].name} has died")
            del players[target]

    #  Check if enemy has won
    if len(players) == 0:
        print(f"{Bcolors.BOLD}{Bcolors.FAIL}Your enemy has defeated you. YOU LOST!!!{Bcolors.ENDC}")
        running = False



#todo: when you go back up one level it should actually go back up one level and not skip to the next person
#todo: handle when the user enters a wrong input
