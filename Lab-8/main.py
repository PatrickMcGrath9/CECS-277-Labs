# Names: Patrick Mc Grath & Julianna De Joya
# Date: 10/9/2023
# Desc: This program allows the user to play a game in which they must defeat 3 dragons. The user cannot lose their health, or else they lose the trials.


import check_input
import random
import dragon
import fire_dragon
import flying_dragon
import hero


def main():
    name = input("What is your name, challenger?\n")  # prompts user to enter their name
    print(f"Welcome to dragon training, {name}\nYou must defeat 3 dragons.\n")
    user_hero = hero.Hero(name, 50)

    Dragon = dragon.Dragon("Deadly Nadder", 10)  # lists the dragons the user must defeat
    FireDragon = fire_dragon.FireDragon("Gronckle", 15, 3)
    FlyingDragon = flying_dragon.FlyingDragon("Timberjack", 20, 5)
    dragons = [Dragon, FireDragon, FlyingDragon]

    while user_hero.hp > 0 and len(
            dragons) > 0:  # user can proceed with the game while hp is above 0 and dragons are still alive
        print(user_hero)
        count_dragons = 1

        for dragon_object in dragons:
            if dragon_object.hp == 0:
                continue
            print(f"{count_dragons}. Attack {dragon_object}")
            count_dragons += 1

        dragon_choice = check_input.get_int_range("Choose a dragon to attack: ", 1,
                                                  count_dragons - 1)  # prompts user to choose dragon to attack
        print()

        print(f"Attack with:\n1. Sword (2 D6)\n2. Arrow (1 D12)")
        weapon_choice = check_input.get_int_range("Enter weapon: ", 1, 2)  # prompts user to choose weapon
        print()

        dragon_attack_choice = random.randint(1, 2)  # dragon attack is randomly selected

        if weapon_choice == 1:  # hero performs basic attack (sword)
            print(user_hero.basic_attack(dragons[dragon_choice - 1]))
            for dragon_object in dragons:  # removes dragon when hp is 0
                if dragon_object.hp == 0:
                    dragons.remove(dragon_object)

            if dragon_attack_choice == 1 and len(dragons) != 0:
                print(dragons[random.randint(0, len(dragons) - 1)].basic_attack(user_hero))
            elif len(dragons) != 0:
                print(dragons[random.randint(0, len(dragons) - 1)].special_attack(user_hero))


        elif weapon_choice == 2:  # hero performs special attack (arrow)
            print(user_hero.special_attack(dragons[dragon_choice - 1]))
            for dragon_object in dragons:  # removes dragon when hp is 0
                if dragon_object.hp == 0:
                    dragons.remove(dragon_object)

            if dragon_attack_choice == 1 and len(dragons) != 0:
                print(dragons[random.randint(0, len(dragons) - 1)].basic_attack(user_hero))
            elif len(dragons) != 0:
                print(dragons[random.randint(0, len(dragons) - 1)].special_attack(user_hero))

    if len(dragons) == 0:
        print(
            "\nCongratulations! You have defeated all 3 dragons, you have passed the trials.")  # displays when user has defeated all dragons

    if user_hero.hp == 0:
        print(
            "You have been defeated by the dragons, you have failed the trials.")  # displays when user's hp is depleted


main()
