class Card():
  '''Sets the suit and rank of cards and compares them
  Attributes:
    _rank (int): index 0-12, representing card ranks
    _suit (int): index 0-3, representing card suits'''

  
  def __init__ (self, suit, rank):
    '''assign the parameters to the attributes'''
    self._suit = suit
    self._rank = rank

  
  @property
  def rank(self):
    '''decorator used to make property for the _rank attribute'''
    return self._rank

  
  def __str__ (self):
    '''return string in the following format: "rank of suit"'''
    ranks = ['2', '3', '4', '5', '6', '7', '8', '9', '10', 'Jack', 'Queen', 'King', 'Ace']
    suits = ['Clubs', 'Diamonds', 'Hearts', 'Spades']
    rank_of_suit = ranks[self.rank] + " of " + suits[self._suit]
    return rank_of_suit


  def __lt__ (self, other):
    '''compates the ranks of the self and other cards'''
    return self.rank < other.rank
