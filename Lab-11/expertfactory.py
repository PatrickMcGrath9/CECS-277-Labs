import enemyfactory
import zombie
import skeleton
import goblin
import random

class ExpertFactory(enemyfactory.EnemyFactory):
  '''creates difficult enemies and randomly selects one'''

  def create_random_enemy(self):
    '''randomizes and constructs one of the difficult enemies'''
    difficult_enemy_list = [zombie.Zombie(), skeleton.Skeleton(), goblin.Goblin()]
    difficult_enemy = random.choice(difficult_enemy_list)
    return difficult_enemy