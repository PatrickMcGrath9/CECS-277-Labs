import entity
import random


class EasyZombie(entity.Entity):
    '''zombie enemy
        Attributes:
          _max_hp - hp of enemy'''

    def __init__(self):
        '''randomize max_hp, use super to initialize name and max_hp'''
        self._max_hp = random.randint(4, 5)
        super().__init__('Zombie', self._max_hp)

    def attack(self, entity):
        '''enemy attacks hero with random damage'''
        damage = random.randint(1, 5)
        entity.take_damage(damage)
        return f"{self._name} attacks a {entity._name} for {damage} damage."