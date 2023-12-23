# Names: Patrick Mc Grath & Julianna De Joya
# Date: 10/2/2023
# Desc: This program will create a game of Blackjack in which the user plays against the computer as the "Player" and "Dealer," respectively. The Player and Dealer's card values are added up, and whoever has the highest score without going over 21 wins a point.


import check_input
from deck import Deck
from player import Player
from dealer import Dealer

def display_winner(pScore, dScore, points):
  '''displays the winner of the round based on the player's and dealer's hand scores'''
  if pScore == dScore or (pScore > 21 and dScore > 21):
    print("Tie")                                             # tie if the Player and Dealer's scores are the same
  elif pScore > 21 or (dScore <= 21 and dScore > pScore):
    print("Dealer wins.")                                    # Dealer wins if they have higher score, where the score is less than 21
    points[1] += 1
  elif dScore > 21 or (pScore <= 21 and pScore > dScore):
    print("Player wins.")                                    # Player wins if they have higher score, where the score is less than 21
    points[0] += 1

def main():
  print("-Blackjack-")
  points = [0, 0]

  deck = Deck()
  deck.shuffle()                                             # shuffles deck

  while True:
    if len(deck) < 15:
      deck = Deck()
      deck.shuffle()
    player = Player(deck)
    print(player)

    while True:
      choice = check_input.get_int_range("1. Hit\n2. Stay\nEnter choice: ", 1, 2)    # prompts user to enter choice
      if choice == 1:                                                                # if user selects 1, add card to hand
        player.hit()
        print(player)
        if player.score() > 21:                                                      # if score is greater than 21, print "Bust"
          print("Bust!")
          break
      elif choice == 2:                                                              # if user selects 2, stop program
        break

    dealer = Dealer(deck)
    print(dealer.play())

    display_winner(player.score(), dealer.score(), points)                           # displays winner
    print(f"Player's points: {points[0]}\nDealer's points: {points[1]}")

    play_again = check_input.get_yes_no("Play again? (Y/N): ")                       # user responds "Y" or "N" to playing another round
    if play_again != True:
      break



main()