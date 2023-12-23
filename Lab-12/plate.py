import abc

class Plate(abc.ABC):
  '''abstract interface'''

  @abc.abstractmethod
  def description(self):
    pass

  @abc.abstractmethod
  def area(self):
    pass

  @abc.abstractmethod
  def weight(self):
    pass

  @abc.abstractmethod
  def count(self):
    pass
  