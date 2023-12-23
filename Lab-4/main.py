# Names: Patrick Mc Grath & Julianna De Joya
# Date: 9/11/2023
# Desc: This program will allow the user to move through a maze, prompting the user to move north, west, east or south. The user must go from point 's' to point 'f.'

import check_input


def read_maze():
    '''Reads contents of maze fule and stores the contents in a 2D list'''

    maze = open("maze2-1.txt")  # opens maze file
    maze_2dlist_read = []  # sets up empty 2d list
    for row in maze:
        list = []
        for char in row:
            if char != '\n':
                list.append(char)
        maze_2dlist_read.append(list)  # stores contents of file in 2d list
    return maze_2dlist_read  # returns filled 2d list


def find_start(maze):
    '''Locates 's' in the given text file and identifies it as the start location, returning the location as a 1D list'''

    for row in range(len(maze)):
        for colm in range(len(maze[row])):
            if maze[row][colm] == 's':  # confirms location of 's'
                return [row, colm]  # returns location of 's'


def display_maze(maze, loc):
    '''Displays each character in the maze text file in a matrix format, and uses 'X' to display the user's location'''

    for row in range(len(maze)):
        for colm in range(len(maze[row])):
            if row == loc[0] and colm == loc[1]:
                print('X', end='')  # displayed 'X' for user's locaiton
            else:
                print(maze[row][colm], end='')
        print()


def main():
    print("-Maze Solver-")

    maze_2Dlist = read_maze()
    start_loc = find_start(maze_2Dlist)
    user_loc = start_loc  # initialize users location as the start location

    user_end = False

    while user_end == False:
        display_maze(maze_2Dlist, user_loc)  # displays maze and user's location

        print("1. Go North")  # menu that prompts player to enter direction to go in
        print("2. Go South")
        print("3. Go East")
        print("4. Go West")

        user_choice = check_input.get_int_range("Enter choice: ", 1,
                                                4)  # prompts user to enter choice on which direction to go
        next_loc = [user_loc[0], user_loc[1]]  # updated location

        if user_choice == 1:
            next_loc[0] = next_loc[0] - 1  # user ('X') moves one space North

        elif user_choice == 2:
            next_loc[0] = next_loc[0] + 1  # user ('X') moves one space South

        elif user_choice == 3:
            next_loc[1] = next_loc[1] + 1  # user ('X') moves one space East

        else:
            next_loc[1] = next_loc[1] - 1  # user ('X') moves one space West

        if maze_2Dlist[next_loc[0]][next_loc[1]] == '*':
            print("You cannot move there.")  # this statement prints if user tries to move through wall


        else:
            user_loc = next_loc
            if maze_2Dlist[user_loc[0]][user_loc[1]] == 'f':
                display_maze(maze_2Dlist, user_loc)
                print("Congratulations! You Solved the maze.")  # this statement prints if user makes it to finish ('f')
                user_end = True


main()