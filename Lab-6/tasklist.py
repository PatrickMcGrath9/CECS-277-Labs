import task


class Tasklist:
    ''' Initializes a list that holds all of the users' tasks in which tasks can be added or marked complete
    Attributes:
      user_tasklist (list): A list of users' tasks
    '''

    def __init__(self):
        '''reads in, stores, and sorts list of tasks to tasklist.txt'''
        self.user_tasklist = []
        task_file = open("tasklist.txt", "r")
        tasks = task_file.readlines()
        for line in tasks:
            current_task = line.strip().split(",")
            user_task = task.Task(current_task[0], current_task[1], current_task[2])
            self.user_tasklist.append(user_task)  # appends tasks
        self.user_tasklist = sorted(self.user_tasklist)  # sorts tasks

    def add_task(self, desc, date, time):
        '''adds task to tasklist and sorts the task according to due date and time'''
        self.user_tasklist.append(
            task.Task(desc, date, time))  # appends tasks (including the task description, due data, and time)
        self.user_tasklist = sorted(self.user_tasklist)  # sorts tasks by due date and time

    def mark_complete(self):
        '''marks the current task as completed by removing it from the tasklist'''
        self.user_tasklist.remove(self.user_tasklist[0])  # removes the current task

    def save_file(self):
        '''writes the contents of the task list to the file and ends the program'''
        tasklist = open("tasklist.txt", "w")
        if len(self.user_tasklist) > 0:
            for num_objects in range(len(self.user_tasklist) - 1):
                tasklist.write(repr(self.user_tasklist[num_objects]) + "\n")
            tasklist.write(repr(self.user_tasklist[len(self.user_tasklist) - 1]))
            tasklist.close()

    def __getitem__(self, index):
        '''returns the task at the given index'''
        return self.user_tasklist[index]

    def __len__(self):
        '''returns the length of the task list'''
        return len(self.user_tasklist)

