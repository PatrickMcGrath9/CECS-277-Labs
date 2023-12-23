# Names: Patrick Mc Grath & Julianna De Joya
# Date: 10/16/2023
# Desc: This program acts as an escape room which prompts the user to make choices to open 3 types of doors , namely the Basic Door, the Locked Door, and the Combo Door.


from basic_door import BasicDoor
from combo_door import ComboDoor
from locked_door import LockedDoor
import check_input
import random


def open_door(door):
  '''creates a door object and prompts the user to select a menu option to unlock the door'''
  door_object = door()
  print(door_object.examine_door())
  
  while door_object.is_unlocked() == False:
    print(door_object.menu_options())
    user_option = check_input.get_int_range("", 1, door_object.get_menu_max())
    print(door_object.attempt(user_option))
    
    if door_object.is_unlocked() == True:
      print(door_object.success())
      
    elif door_object.is_unlocked() == False:
      print(door_object.clue())
  


def main():

  print("Welcome to the Escape Room.")
  print("You must unlock 3 doors to escape...")
  
  door_list = [BasicDoor, LockedDoor, ComboDoor]          # List of door types

  count = 1

  while count < 4:
    door_choice = random.choice(door_list)          # Randomly selects a door type
    open_door(door_choice)
    print()
    count += 1

  print("Congratulations! You escaped... this time.")
  






main()