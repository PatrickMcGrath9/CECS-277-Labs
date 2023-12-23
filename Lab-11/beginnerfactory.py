import enemyfactory
import easyzombie
import easyskeleton
import easygoblin
import random

class BeginnerFactory(enemyfactory.EnemyFactory):
  '''creates enemies and randomly selects one'''

  def create_random_enemy(self):
    '''randomizes and constructs one of the easy enemies'''
    easy_enemy_list = [easyzombie.EasyZombie(), easyskeleton.EasySkeleton(), easygoblin.EasyGoblin()]
    easy_enemy = random.choice(easy_enemy_list)
    return easy_enemy