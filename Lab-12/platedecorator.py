import abc
import plate

class Platedecorator(plate.Plate, abc.ABC):
  '''extends ABC and extends from Plate
      Attributes:
        _plate - plate object'''
  
  def __init__(self, p):
    '''pass in plate p'''
    self._plate = p

  def description(self):
    '''call on _plate attribute'''
    return self._plate.description()
    
  def area(self):
    '''call on _plate attribute'''
    return self._plate.area()

  def weight(self):
    '''call on _plate attribute'''
    return self._plate.weight()

  def count(self):
    '''call on _plate attribute'''
    return self._plate.count()