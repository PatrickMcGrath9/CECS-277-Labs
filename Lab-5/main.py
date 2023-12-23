# Names: Patrick Mc Grath & Julianna De Joya
# Date: 9/18/2023
# Desc: This program allows the user to input the dimension of a rectangle and move through said rectangle in a grid.

import check_input
import rectangle



def display_grid(grid):
  '''passes and displays contents of grid'''
  for row in grid:
    for column in row:
      print(column, end = "")
    print()

def reset_grid(grid):
  '''passes in grid and overwrites content with "."'''
  for row in range(len(grid)):
    for column in range(len(grid[row])):
      grid[row][column] = "."  

def place_rect(grid, rect):
  '''passes in grid and rectangle, with "*" being used for the rectangle'''
  for row in range(rect[1]):
    for column in range(rect[0]):
      grid[row + rect[3]][column + rect[2]] = "*"
  

def main():
  rectangle_grid = []
  for row in range(20):
    row_list = []
    for column in range(20):
      row_list.append(".")
    rectangle_grid.append(row_list)


  rec_width = check_input.get_int_range("Enter rectangle width (1-5): ", 1, 5)      # prompts user to enter rectangle width
  rec_height = check_input.get_int_range("Enter rectangle height (1-5): ", 1, 5)    # prompts user to enter rectangle height

  user_rectangle = rectangle.Rectangle(rec_width, rec_height)                       # rectangle that user can move
  dimensions = user_rectangle.get_dimensions()                                      # desired dimensions of the user

  rec_coords = user_rectangle.get_coords()                                          # the rectangle's initial coordinates

  dimensions_and_coords = dimensions + rec_coords                                   # dimensions of the rectangle and initial coordinates

  place_rect(rectangle_grid, dimensions_and_coords)                                 # places rectangle at initial coordinates

  user_quit = False

  while user_quit == False:

    print()
    
    display_grid(rectangle_grid)

    print()
    print("Enter Direction")                                          # menu that displays what choices the user can make
    print("1. Up")
    print("2. Down")
    print("3. Left")
    print("4. Right")
    print("5. Quit")

    user_choice = check_input.get_int_range("", 1, 5)                # prompts the user to choose a direction or quit

    
    if user_choice == 1:                                             # the user's rectangle moves up
      if rec_coords[1] == 0:
        print("Out of bounds. Try again")
      else:
        user_rectangle.move_up()
      

    if user_choice == 2:                                             # the user's rectangle moves down
      if rec_coords[1] == len(rectangle_grid) - dimensions[1]:
        print("Out of bounds. Try again")
      else:
        user_rectangle.move_down()

    if user_choice == 3:                                             # the user's rectangle moves left
      if rec_coords[0] == 0:
        print("Out of bounds. Try again")
      else:
        user_rectangle.move_left()

    if user_choice == 4:                                             # the user's rectangle moves right
      print(len(rectangle_grid[0]))
      if rec_coords[0] == len(rectangle_grid[0]) - dimensions[0]:
        print("Out of bounds. Try again")
      else:
        user_rectangle.move_right()

    if user_choice == 5:                                             # the user quits and the program stops
      user_quit = True

    rec_coords = user_rectangle.get_coords()                         # new rectangle coordinates after user moves

    dimensions_and_coords = dimensions + rec_coords                  # dimensions of the rectangle and new coordinates
    
    reset_grid(rectangle_grid)                                       # resets grid in which rectangle moves
    
    place_rect(rectangle_grid, dimensions_and_coords)                # places rectangle with new coordinates



main()