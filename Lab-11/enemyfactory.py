import abc


class EnemyFactory(abc.ABC):
    '''abstract enemy factory to make differnt difficulty types'''

    @abc.abstractmethod
    def create_random_enemy(self):
        pass