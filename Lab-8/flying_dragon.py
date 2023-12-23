import dragon
import random


class FlyingDragon(dragon.Dragon):
    '''inherits from Dragon'''

    def __init__(self, name, max_hp, swoops):
        '''call super init to set the name and hp; set the number of swoops'''
        super().__init__(name, max_hp)
        self.swoops = swoops

    def special_attack(self, other):
        '''overridden swoop attack - if there are swoops remaining, hero takes random amount of damage in range 5-8 and number of swoops decrements'''
        if self.swoops > 0:
            swoop_damage = random.randint(5, 8)
            other.take_damage(swoop_damage)
            self.swoops -= 1
            return f"Timberjack does a swoop attack for {swoop_damage} damage!\n"
        else:
            print("There are no swoop attacks remaining, you do not take damage.\n")

    def __str__(self):
        '''get __str__ from entity class and concatenate on the number of swoops'''
        if self.swoops >= 0:
            return super().__str__() + f"\nSwoop attacks remaining: {self.swoops}"
        return super().__str__()