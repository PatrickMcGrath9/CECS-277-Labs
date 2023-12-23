import entity
import random


class Dragon(entity.Entity):
    '''inherits from Entity'''

    def basic_attack(self, other):
        '''tail attack - hero takes random amount of damage from dragon in range 3-7'''
        tail_damage = random.randint(3, 7)
        other.take_damage(tail_damage)
        return f"{self.name} smashes you with its tail for {tail_damage} damage!\n"

    def special_attack(self, other):
        '''claw attack - hero takes random amount of damage from dragon in range 4-8'''
        claw_damage = random.randint(4, 8)
        other.take_damage(claw_damage)
        return f"{self.name} slashes you with its claws for {claw_damage} damage!\n"