import card

class Player():
  '''Uses the passed in deck to construct the player's hand which allows them to hit and see score
  Attributes:
    _deck: reference to the deck of cards that both the player and the dealer use
    _hand: list of Cards that the player is currently holding'''

  
  def __init__(self, deck):
    '''sets deck attribute; deals 2 cards from the deck to the player's hand and then sorts the hand'''
    self._deck = deck
    self._hand = []
    for cards in range(2):
      self._hand.append(self._deck.draw_card())
    self._hand.sort()

  
  def hit(self):
    '''adds another card from the deck to the player's hand and resorts them'''
    top_card = self._deck.draw_card()
    self._hand.append(top_card)
    self._hand.sort()

  
  def score(self):
    '''totals up the cards in the player's hand and then returns the score'''
    score = 0
    for cards in self._hand:
      if cards.rank < 9:
        score += cards.rank + 2                   # cards 2-10 are face value
    for cards in self._hand:
      if cards.rank >= 9 and cards.rank < 12:
        score += 10                               # face cards are worth 10
      elif cards.rank == 12:
        if score + 11 <= 21:
          score += 11                             
        else:
          score += 1                              # ace card is worth 1 or 11
    return score

  
  def __str__(self):
    '''displays each of the cards in the player's hand and returns the score'''
    hand = ""
    for cards in self._hand:
      hand += str(cards) + "\n"
    return f"\nPlayer's Cards:\n{hand}Score = {self.score()}"