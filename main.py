# Name: Patrick Mc Grath & Julianna De Joya
# Date: 8/23/2023
# Desc: This program will generate a random int between 1-100 and will make # the user guess until they get the correct number.

import random
import check_input

def main():
  # Generating a random value for our function with a counter "tries" for the number of guesses
  random_val = random.randint(1, 100);
  tries = 0

  # Adding the title along with the first iteration of the user guessing while incrementing tries
  print("- Guessing Game -")
  user_val = check_input.get_int_range("I'm thinking of a number. Make a guess (1-100): ", 1, 100)
  tries += 1

  # A while loop which iterates until the the user guesses the random value depending whether it is lower or higher
  while (user_val != random_val):
      if user_val < random_val:
        print("Too low! ", end="")
        random_val += 1
        user_val = check_input.get_int_range("Guess again (1-100): ", 1, 100)

      elif user_val > random_val:
        print("Too high! ", end="")
        tries += 1
        user_val = check_input.get_int_range("Guess again (1-100): ", 1, 100)

  # Prints the number of correct interations/tries the user guessed the correct number
  print("Correct!  You got it in " + str(tries) + " tries.")

main()
