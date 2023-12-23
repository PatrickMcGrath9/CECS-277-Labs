import entity
import random

class Enemy(entity.Entity):
  '''extends entity - monster character that the hero encounters'''

  def __init__(self):
    '''randomizes list of monster names and their hp'''
    list_names = ['Goblin', 'Vampire', 'Ghoul', 'Skeleton', 'Zombie']
    self._name = random.choice(list_names)
    self._max_hp = random.randint(4, 8)
    self._hp = self._max_hp

  def attack(self, entity):
    '''enemy attacks hero with random damage from 1-4'''
    damage = random.randint(1, 4)
    entity.take_damage(damage)
    return f"{self._name} attacks a {entity._name} for {damage} damage."