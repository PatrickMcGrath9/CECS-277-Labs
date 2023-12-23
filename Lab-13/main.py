# Names: Patrick Mc Grath & Julianna De Joya
# Date: 11/29/2023
# Desc: This program will allow the user to manage a task list. The user will be able to view, list, and add tasks, as well as mark any completed tasks and search tasks by date.

#from typing import ParamSpecArgs
import check_input
import tasklist

def main_menu():
  '''displays menu from which the user can select how to manage the task list'''
  # options
  print("1. Display current task")
  print("2. Display all tasks")
  print("3. Mark current task complete")
  print("4. Add new task")
  print("5. Search by date")
  print("6. Save and quit")
  #prompts user to enter their choice
  return check_input.get_int_range("Enter choice: ", 1, 6)


def get_date():
  '''prompts the user to enter the month, day, and year for the task's due date and formats it as MM/DD/YY'''
  enter_month = check_input.get_int_range("Enter month: ", 1, 12)
  enter_day = check_input.get_int_range("Enter day: ", 1, 31)
  enter_year = check_input.get_int_range("Enter year: ", 2000, 3000)

  # if the number entered is less than 10, 0 is added to the front
  if enter_month < 10:
    enter_month = "0" + str(enter_month)
  if enter_day < 10:
    enter_day = "0" + str(enter_day)

  # formats the date as MM/DD/YY
  date = f"{enter_month}/{enter_day}/{enter_year}"
  return date


def get_time():
  '''prompts the user to enter the hour and minutes for the task's time and formats it as HH:MM'''
  print("Enter time:")
  enter_hour = check_input.get_int_range("Enter hour: ", 0, 23)
  enter_minute = check_input.get_int_range("Enter minute: ", 0, 59)

  # if the number enteres is less than 10, 0 is added to the front
  if enter_hour < 10:
    enter_hour = "0" + str(enter_hour)
  if enter_minute < 10:
    enter_minute = "0" + str(enter_minute)

  # formats the time as HH:MM
  time = f"{enter_hour}:{enter_minute}"
  return time


def main():

  user_option = 0
  user_tasks = tasklist.Tasklist()

   # while the program is running, the header and tasks to complete are displayed
  while user_option != 6:

    print("-Tasklist-")
    print("Tasks to complete:", len(user_tasks))

    # stores current task as the task with the closest due date and time
    if len(user_tasks) != 0:
      current_task = user_tasks.get_current_task()

    user_option = main_menu()

    # displays current task
    if user_option == 1:
      if len(user_tasks) == 0:
        print("All tasks completed")
      else:
        print("Current task is:")
        print(current_task)

    # displays all tasks
    elif user_option == 2:
      if len(user_tasks) == 0:
        print("All tasks completed")
      else:
        print("Tasks:")
        for object in user_tasks:
          print(object, end = "\n")

    # marks current task as completed
    elif user_option == 3:
      if len(user_tasks) == 0:
        print("All tasks completed")
      else:
        print("Marking current task as complete:")
        print(current_task)
        user_tasks.mark_complete()
        if len(user_tasks) == 0:
          print("All tasks completed")
        else:
          current_task = user_tasks.get_current_task()
          print("New current task is:")
          print(current_task._desc, "- Due:", current_task._date, "at", current_task._time)

    # add new task
    elif user_option == 4:
      task = input("Enter a task: ")
      print("Enter due date:")
      date = get_date()
      time = get_time()
      user_tasks.add_task(task, date, time)

    # searches tasks by date and prints them
    elif user_option == 5:
      num = 1
      print("Enter date to search:")
      search_date = get_date()
      print(f"Tasks due on {search_date}: ")
      for task in user_tasks:
        if task._date == search_date:
          print(f"{num}.", task._desc, "- Due:", task._date, "at", task._time)
          num += 1

    #save and quit program
    elif user_option == 6:
      user_tasks.save_file()

    print()




main()