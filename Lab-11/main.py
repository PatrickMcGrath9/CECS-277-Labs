# Names: Patrick Mc Grath & Julianna De Joya
# Date: 11/8/2023
# Desc: This program allows the user to go through a maze with different
# areas with enemies and items, their goal is to get to the finish. This
# updated version includes new maps and a difficulty setting.


import check_input
import hero
import map
import beginnerfactory
import expertfactory
import random


def main():
    name = input("What is your name, traveler? ")  # prompts user to enter name
    user_hero = hero.Hero(name)
    maze = map.Map()
    directions = [user_hero.go_north, user_hero.go_south, user_hero.go_east, user_hero.go_west]
    map_num = 1

    difficulty = check_input.get_int_range("Difficulty: \n1. Beginner \n2. Expert\n", 1, 2)

    while user_hero.hp > 0:
        maze.reveal(user_hero.loc)
        print(user_hero)
        print(maze.show_map(user_hero.loc))

        print("1. Go North")  # menu options
        print("2. Go South")
        print("3. Go East")
        print("4. Go West")
        print("5. Quit")
        user_choice = check_input.get_int_range("Enter choice: ", 1, 5)  # prompts user to choose direction

        if user_choice == 1:
            result = user_hero.go_north()
        elif user_choice == 2:
            result = user_hero.go_south()
        elif user_choice == 3:
            result = user_hero.go_east()
        elif user_choice == 4:
            result = user_hero.go_west()
        elif user_choice == 5:
            print("Game Over")
            break

        if result == 'm':  # monster
            maze.reveal(user_hero.loc)
            if difficulty == 1:
                enemy_encounter = beginnerfactory.BeginnerFactory().create_random_enemy()
            else:
                enemy_encounter = expertfactory.ExpertFactory().create_random_enemy()
            print(f"You encounter a ", end='')
            print(enemy_encounter)
            while enemy_encounter.hp > 0 and user_hero.hp > 0:
                print(f"1. Attack {enemy_encounter.name}")
                print("2. Run away")
                user_choice_enemy = check_input.get_int_range("Enter choice: ", 1, 2)
                if user_choice_enemy == 1:
                    print(user_hero.attack(enemy_encounter))
                    if enemy_encounter.hp <= 0:
                        break
                    if enemy_encounter.hp > 0:
                        print(enemy_encounter.attack(user_hero))
                    if user_hero.hp <= 0:
                        print(f"You died! \nGame Over")
                        break
                elif user_choice_enemy == 2:
                    choice = random.randint(1, 4)
                    if choice == 1:
                        user_hero.go_north()
                    elif choice == 2:
                        user_hero.go_south()
                    elif choice == 3:
                        user_hero.go_east()
                    elif choice == 4:
                        user_hero.go_west()
                    print("You ran away!\n")
                    break

            if user_hero.hp <= 0:
                break

            if enemy_encounter.hp <= 0:
                maze.remove_at_loc(user_hero.loc)
                print(f"You have slain a {enemy_encounter.name}\n")



        elif result == 'o':  # invalid direction
            print("You can not go that way...\n")

        elif result == 'n':  # nothing
            maze.reveal(user_hero.loc)
            print("There is nothing here...\n")

        elif result == 's':  # start
            maze.reveal(user_hero.loc)
            print("You're back where you started.\n")

        elif result == 'i':  # item room
            maze.reveal(user_hero.loc)
            print("You found a health potion! You drink it to restore your health.\n")
            user_hero.heal()
            maze.remove_at_loc(user_hero.loc)

        elif result == 'f':  # finish/new map
            maze.reveal(user_hero.loc)
            print("Congratulations! You found the stairs to the next floor of the dungeon.")
            map_num += 1
            if map_num >= 4:
                map_num = 1
            maze.load_map(map_num)


main()