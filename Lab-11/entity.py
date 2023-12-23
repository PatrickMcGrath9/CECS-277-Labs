import abc

class Entity(abc.ABC):
  '''Abstract class
      Attributes:
        _name - entity's name
        _hp - entity's hit points
        _max_hp - entity's starting hit points'''


  def __init__(self, name, max_hp):
    '''set _name, _max_hp, and _hp'''
    self._name = name
    self._max_hp = max_hp
    self._hp = max_hp


  @property
  def name(self):
    '''decorator'''
    return self._name


  @property
  def hp(self):
    '''decorator'''
    return self._hp


  def take_damage(self, dmg):
    '''damage the entity takes'''
    self._hp -= dmg
    if self._hp < 0:
      self._hp = 0


  def heal(self):
    '''restores the entity's hp to max_hp'''
    self._hp = self._max_hp


  def __str__(self):
    '''display entity's name and hp'''
    return f"{self._name}\nHP: {self._hp}/{self._max_hp}"


  @abc.abstractmethod
  def attack(self, entity):
    '''abstract method'''
    pass