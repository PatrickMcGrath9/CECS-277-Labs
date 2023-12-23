# Names: Patrick Mc Grath & Julianna De Joya
# Date: 9/6/2023
# Desc: This program will create a two-player dice game in which the objective is to first obtain rolls of 6, 5, and 4. The remaining dice are used as the player's points.

import check_input
import random

def roll_dice(dice):
  '''A list of dice is passed with values 1-6. The values are randomized, sorted, and placed in descending order'''
  
  for dice_number in range(len(dice)):
    dice[dice_number] = random.randint(1, 6)    # randomizes dice value from range 1-6
  dice.sort(reverse = True)                     # sorts the list values from greatest to lowest
  

def display_dice(name, dice):
  '''The name of the list and the list of values of the dice are passed.'''

  print(name + " = ", end= "")                        # passes in name of the list
  for dice_values in range(len(dice)):                
    print(str(dice[dice_values]) + " ", end= "")      # displays dice values with spaces in between
  print()


def find_winner(player_points):
  '''The two player's points are passed as a list, and the points values and winner are displayed'''

  player_1_score = player_points[0]
  player_2_score = player_points[1]

  print()
  print("Score:")
  print("Player #1 =", player_1_score)
  print("Player #2 =", player_2_score)
  if player_1_score == player_2_score:                # checks if player scores are tied
    print("Player #1 and Player #2 are tied.")
    print()
  elif player_1_score > player_2_score:               # if player 1 has a greater score, they win
    print("Player #1 won!")
    print()
  else:                                               # if player 1 has a greater score, they win
    print("Player #2 won!")
    print()


def main():
  print("- Ship, Captain, and Crew! -")

  player_scores = []        # list to store two player's scores
  keep = []                 # list to store dice to keep
  roll = []                 # list to store dice to roll

  player_1_score = 0
  player_2_score = 0
  play_again = True
  
  for player in range(2):                                  # for loop repeats twice for player 1 and 2
    keep = []                                           
    roll = [1, 2, 3, 4, 5]                                 # roll list has len(5)

    print()
    print("Player #" + str(player + 1) + "'s Turn:")       # displays who's turn it is

    for rounds in range(3):                  
      roll_dice(roll)
      display_dice("Roll", roll)

      # if 6 was rolled, 6 is added to keep list and removed from roll list
      if 6 in roll and 6 not in keep:                     
        keep.append(6)
        roll.remove(6)
        print("Yo ho ho! Ye secured a ship!")
      # if 5 was rolled, 5 is added to keep list and removed from roll list
      if 5 in roll and 5 not in keep and (6 in keep or 6 in roll):  
        keep.append(5)
        roll.remove(5)
        print("Shiver me timbers! A Capt'n!")
      # if 4 was rolled, 4 is added to keep list and removed from roll list
      if 4 in roll and 4 not in keep and (6 in keep or 6 in roll) and (5 in keep or 5 in roll):  
        keep.append(4)
        roll.remove(4)
        print("Ye bribed a crew with Grog!")

      display_dice("Keep", keep)                                 # displays the keep list

      if 6 in keep and 5 in keep and 4 in keep:                  # checks that 6, 5, and 4 were rolled
        display_dice("Cargo", roll)

        cargo = sum(roll)
        print("Your cargo points are: " + str(cargo))            # adds and displays cargo points

        if player == 0:
          player_1_score = cargo
        else:
          player_2_score = cargo

        if rounds < 2:
          print()
          play_again = check_input.get_yes_no("Roll again? ")    # prompts player to reply "y" or "no" if they'd like to roll again
          
        if play_again == True:
          continue

        else:
          if player == 0:
            print("Player #" + str(player + 1) + " points = " + str(player_1_score))
            break
          else:
            print("Player #" + str(player + 1) + " points = " + str(player_2_score))
            break

      if rounds < 2:                                             # player is allowed to continue playing if not all numbers were rolled
        print()
        play_again = check_input.get_yes_no("Roll again? ")      # prompts player to reply "y" or "no" if they'd like to roll again
          
        if play_again == True:
          continue

        else:
          if player == 0:
            print("Player #" + str(player + 1) + " points = " + str(player_1_score))
            break
          else:
            print("Player #" + str(player + 1) + " points = " + str(player_2_score))
            break

    else:
      if player == 0:
        print("Player #" + str(player + 1) + " points = " + str(player_1_score))
      else:
        print("Player #" + str(player + 1) + " points = " + str(player_2_score))

  player_scores = [player_1_score, player_2_score]               # list of player's scores
  find_winner(player_scores)

main()