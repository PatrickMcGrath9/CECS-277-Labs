import entity
import random


class Hero(entity.Entity):
    '''inherits from Entity'''

    def basic_attack(self, other):
        '''sword attack - dragon takes random amount of damage from hero in range 2D6'''
        damage_1 = random.randint(1, 6)
        damage_2 = random.randint(1, 6)
        other.take_damage(damage_1 + damage_2)
        return f"You slash the {other.name} with your sword for {damage_1 + damage_2} damage!"

    def special_attack(self, other):
        '''arrow attack - dragon takes random amount of damage from hero in range 1D12'''
        damage = random.randint(1, 12)
        other.take_damage(damage)
        return f"You hit the {other.name} with an arrow for {damage} damage!"