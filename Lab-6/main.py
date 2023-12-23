# Names: Patrick Mc Grath & Julianna De Joya
# Date: 9/25/2023
# Desc: This program will allow the user to manage a task list. The user will be able to view, list, and add tasks, as well as mark any completed tasks.

from typing import ParamSpecArgs
import check_input
import tasklist


def main_menu():
    '''displays menu from which the user can select how to manage the task list'''

    print("1. Display current task")
    print("2. Display all tasks")
    print("3. Mark current task complete")
    print("4. Add new task")
    print("5. Save and quit")
    return check_input.get_int_range("Enter choice: ", 1, 5)  # prompts user to enter their choice


def get_date():
    '''prompts the user to enter the month, day, and year for the task's due date and formats it as MM/DD/YY'''

    print("Enter due date: ")
    enter_month = check_input.get_int_range("Enter month: ", 1, 12)
    enter_day = check_input.get_int_range("Enter day: ", 1, 31)
    enter_year = check_input.get_int_range("Enter year: ", 2000, 3000)

    if enter_month < 10:  # if the month is less than 10, a 0 is added to the front
        enter_month = "0" + str(enter_month)
    if enter_day < 10:  # if the day is less than 10, a 0 is added to the front
        enter_day = "0" + str(enter_day)

    date = f"{enter_month}/{enter_day}/{enter_year}"  # formats the date as follows: MM/DD/YY
    return date


def get_time():
    '''prompts the user to enter the hour and minutes for the task's time and formats it as HH:MM'''

    print("Enter time:")
    enter_hour = check_input.get_int_range("Enter hour: ", 0, 23)
    enter_minute = check_input.get_int_range("Enter minute: ", 0, 59)

    if enter_hour < 10:  # if the hour is less than 10, a 0 is added to the front
        enter_hour = "0" + str(enter_hour)

    if enter_minute < 10:  # if the minutes are less than 10, a 0 is added to the front
        enter_minute = "0" + str(enter_minute)

    time = f"{enter_hour}:{enter_minute}"  # formats the time as follows: HH:MM
    return time


def main():
    user_option = 0
    user_tasks = tasklist.Tasklist()

    while user_option != 5:  # while the program is running, the header and tasks to complete are displayed

        print("-Tasklist-")
        print("Tasks to complete:", len(user_tasks))

        if len(user_tasks) != 0:
            current_task = user_tasks[0]  # stores current task as the task with the closest due date and time

        user_option = main_menu()

        if user_option == 1:
            if len(user_tasks) == 0:
                print("All tasks completed")
            else:
                print("Current task is:")
                print(current_task.desc, "- Due:", current_task.date, "at", current_task.time)


        elif user_option == 2:
            if len(user_tasks) == 0:
                print("All tasks completed")
            else:
                print("Tasks:")
                for object in user_tasks:
                    print(object.desc, "- Due:", object.date, "at", object.time, end="\n")


        elif user_option == 3:
            if len(user_tasks) == 0:
                print("All tasks completed")
            else:
                print("Marking current task as complete:")
                print(current_task.desc, "- Due:", current_task.date, "at", current_task.time)
                user_tasks.mark_complete()
                if len(user_tasks) == 0:
                    print("All tasks completed")
                else:
                    current_task = user_tasks[0]
                    print("New current task is:")
                    print(current_task.desc, "- Due:", current_task.date, "at", current_task.time)

        elif user_option == 4:
            task = input("Enter a task: ")
            date = get_date()
            time = get_time()
            user_tasks.add_task(task, date, time)

        elif user_option == 5:
            user_tasks.save_file()

        print()


main()