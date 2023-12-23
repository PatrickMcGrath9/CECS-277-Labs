import door
import check_input
import random

class ComboDoor(door.Door):

  def __init__(self):
    self._key_combo = random.randint(1, 10)
    self._user_option = 0

  def examine_door(self):
    '''returns a string description of the door'''
    return "You encounter a door with a combination lock, you can spin the dial to a number 1-10."

  def menu_options(self):
    '''returns a string of menu options'''
    return "Enter a number 1-10: "

  def get_menu_max(self):
    '''returns the number of menu options'''
    return 10

  def attempt(self, option):
    '''returns a string describing what the user attempted'''
    self._user_option = option
    if option == 1:
      return "You turn the dial to ... 1"
    if option == 2:
      return "You turn the dial to ... 2"
    if option == 3:
      return "You turn the dial to ... 3"
    if option == 4:
      return "You turn the dial to ... 4"
    if option == 5:
      return "You turn the dial to ... 5"
    if option == 6:
      return "You turn the dial to ... 6"
    if option == 7:
      return "You turn the dial to ... 7"
    if option == 8:
      return "You turn the dial to ... 8"
    if option == 9:
      return "You turn the dial to ... 9"
    if option == 10:
      return "You turn the dial to ... 10"

  def is_unlocked(self):
    '''returns true or false depending on if the user unlocked the door'''
    if self._key_combo == self._user_option:
      return True
    else:
      return False

  def clue(self):
    '''returns a string to help the user with their next guess'''
    if self._key_combo < self._user_option:
      return "Try a lower value."
    if self._key_combo > self._user_option:
      return "Try a higher value."

  def success(self):
    '''returns a string congratulating the user on unlocking the door'''
    if self.is_unlocked() == True:
      return "You found the correct value and opened the door."