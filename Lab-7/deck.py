import card
import random

class Deck():
  '''Initializes a deck of cards which can be shuffled, cards can be drawn from the deck and the length of the deck can be accesed
  Attributes:
    _cards (list): A list of card objects'''
  
  
  def __init__(self):
    '''initializes deck of 52 cards; 13 ranks, 4 suits each'''
    self._cards = []
    for suit in range(4):                     # 4 suits
      for rank in range(13):                  # 13 ranks
        card_obj = card.Card(suit, rank)
        self._cards.append(card_obj)

  
  def shuffle(self):
    '''shuffles the deck'''
    random.shuffle(self._cards)

  
  def draw_card(self):
    '''removes topmost card and returns it'''
    return self._cards.pop(0)

  
  def __len__(self):
    '''returns the number of cards that remain in the deck'''
    return len(self._cards)