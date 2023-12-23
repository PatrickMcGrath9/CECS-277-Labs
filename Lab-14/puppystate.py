import abc

class PuppyState(abc.ABC):
  '''interface'''

  @abc.abstractmethod
  def feed(self, puppy):
    '''feed method - abstract'''
    pass

  @abc.abstractmethod
  def play(self, puppy):
    '''play method - abstract'''
    pass