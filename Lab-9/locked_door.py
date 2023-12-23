import door
import check_input
import random

class LockedDoor(door.Door):

  def __init__(self):
    self._key_location = random.randint(1, 3)
    self._user_option = 0

  def examine_door(self):
    '''returns a string description of the door'''
    return "You encounter a locked door."

  def menu_options(self):
    '''returns a string of menu options'''
    return f"1. Look under the mat\n2. Look under the flower pot\n3. Look under the fake rock."

  def get_menu_max(self):
    '''returns the number of menu options'''
    return 3

  def attempt(self, option):
    '''returns a string describing what the user attempted'''
    self._user_option = option
    if option == 1:
      return "You look under the mat."
    elif option == 2:
      return "You look under the flower pot."
    elif option == 3:
      return "You look under the fake rock."

  def is_unlocked(self):
    '''returns true or false depending on if the user unlocked the door'''
    if self._key_location == self._user_option:
      return True
    else:
      return False

  def clue(self):
    '''returns a string to help the user with their next guess'''
    if self.is_unlocked() == False:
      return "Look somewhere else."

  def success(self):
    '''returns a string congratulating the user on unlocking the door'''
    if self.is_unlocked() == True:
      return "You found the key and unlocked the door."