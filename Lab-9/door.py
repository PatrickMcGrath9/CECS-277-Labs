import abc

class Door(abc.ABC):

  @abc.abstractmethod
  def examine_door(self):
    '''abstract method for examine_door'''
    pass

  @abc.abstractmethod
  def menu_options(self):
    '''abstract method for menu_options'''
    pass

  @abc.abstractmethod
  def get_menu_max(self):
    '''abstract method for get_menu_max'''
    pass

  @abc.abstractmethod
  def attempt(self, option):
    '''abstract method for attempt'''
    pass

  @abc.abstractmethod
  def is_unlocked(self):
    '''abstract method for is_unlocked'''
    pass

  @abc.abstractmethod
  def clue(self):
    '''abstract method for clue'''
    pass

  @abc.abstractmethod
  def success(self):
    '''abstract method for success'''
    pass
  