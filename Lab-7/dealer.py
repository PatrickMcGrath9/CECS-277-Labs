import player

class Dealer(player.Player):
  '''Uses the Player class so that the dealer's cards are displayed and follows the rules of a dealer
  Attributes:
    None '''

  
  def play(self):
    '''plays a round for the dealer'''
    dealer_result = ""
    while True:
      dealer_result += f"\nDealer's Cards:\n"
      for card in self._hand:
        dealer_result += str(card) + "\n"
      dealer_result += f"Score = {self.score()}\n"
            
      if self.score() > 21:
        dealer_result += "Bust!\n"
        break    
      if self.score() >= 17:
        break
            
      self.hit()
      dealer_result += "Dealer Hits!\n"
            
    return dealer_result