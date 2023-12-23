# Names: Patrick Mc Grath & Julianna De Joya
# Date: 12/6/2023
# Desc: This program acts as a puppy simulator in which the user selects whether to feed
# or play with the puppy and the puppy responds based on which state it is in.

import puppy
import check_input


def main():
  p = puppy.Puppy()
  
  print("Congratulation on your new puppy!")

  quit = False
  
  while quit != True:
    print("What would you like to do?")    # menu options
    print("1. Feed the puppy")
    print("2. Play with the puppy")
    print("3. Quit")

    user_choice = check_input.get_int_range("Enter choice: ", 1, 3)
    print()

    if user_choice == 1:                   # user selects to give food
      print(p.give_food())
      
    if user_choice == 2:                   # user selects to play
      print(p.throw_ball())
      
    if user_choice == 3:                   # user selects to quit
      quit = True


main()