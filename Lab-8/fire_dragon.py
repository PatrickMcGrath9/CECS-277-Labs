import dragon
import random


class FireDragon(dragon.Dragon):
    '''inherits from Dragon'''

    def __init__(self, name, max_hp, f_shots):
        '''call super init to set the name and hp; set the number of fire shots'''
        super().__init__(name, max_hp)
        self.f_shots = f_shots

    def special_attack(self, other):
        '''overridden fire attack - if there are fire shots remaining, hero takes random amount of damage in range 5-9 and number of fire shots decrements'''
        if self.f_shots > 0:
            fire_damage = random.randint(5, 9)
            other.take_damage(fire_damage)
            self.f_shots -= 1
            return f"Gronckle enguls you in flames for {fire_damage} damage!\n"
        else:
            print("There are no fire shots remaining, you do not take damage.\n")

    def __str__(self):
        '''get __str__ from entity class and concatenate on the number of fire shots'''
        if self.f_shots >= 0:
            return super().__str__() + f"\nFire Shots remaining: {self.f_shots}"
        return super().__str__()