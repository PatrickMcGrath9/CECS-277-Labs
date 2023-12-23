import door
import check_input
import random

class BasicDoor(door.Door):


  def __init__(self):
    self._key_state = random.randint(1, 2)
    self._user_option = 0

  def examine_door(self):
    '''returns a string description of the door'''
    return "You encounter a basic door, you can either push it or pull it to open."
  
  def menu_options(self):
    '''returns a string of menu options'''
    return f"1. Push\n2. Pull"

  def get_menu_max(self):
    '''returns the number of menu options'''
    return 2

  def attempt(self, option):
    '''returns a string describing what the user attempted'''
    self._user_option = option
    if option == 1:
      return "You push the door."
    if option == 2:
      return "You pull the door."

  def is_unlocked(self):
    '''returns true or false depending on if the user unlocked the door'''
    if self._key_state == self._user_option:
      return True
    else:
      return False

  def clue(self):
    '''returns a string to help the user with their next guess'''
    if self.is_unlocked() == False:
      return "Try the other way."

  def success(self):
    '''returns a string congratulating the user on unlocking the door'''
    if self.is_unlocked() == True:
      return "Congratulations, you opened the door."
