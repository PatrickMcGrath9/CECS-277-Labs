import entity
from map import Map
import random

class Hero(entity.Entity):
  '''Extends the Entity class
  Attributes:
    _loc - hero's location'''

  def __init__(self, name):
    '''initialize name and max_hp, sets hero's starting location'''
    super().__init__(name, max_hp = 25)
    self._loc = [0, 0]

  @property
  def loc(self):
    '''decorator'''
    return self._loc


  def attack(self, entity):
    '''hero attacks enemy with random damage from 2-5'''
    damage = random.randint(2, 5)
    entity.take_damage(damage)
    return f"{self._name} attacks a {entity._name} for {damage} damage."


  def go_north(self):
    '''hero moves north'''
    if self._loc[0] > 0:
      self._loc[0] -= 1
      return Map()[self._loc[0]][self._loc[1]]
    return 'o'
      
  def go_south(self):
    '''hero moves south'''
    if self._loc[0] < len(Map()) - 1:
      self._loc[0] += 1
      return Map()[self._loc[0]][self._loc[1]]
    return 'o'
    
  def go_east(self):
    '''hero moves east'''
    if self._loc[1] < len(Map()) - 1:
      self._loc[1] += 1
      return Map()[self._loc[0]][self._loc[1]]
    return 'o'
    
  def go_west(self):
    '''hero moves west'''
    if self._loc[1] > 0:
      self._loc[1] -= 1
      return Map()[self._loc[0]][self._loc[1]]
    return 'o'


  