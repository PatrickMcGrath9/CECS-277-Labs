import task


class Tasklist:
    ''' Initializes a list that holds all of the users' tasks in which tasks can be added or marked complete
    Attributes:
      user_tasklist (list): A list of users' tasks
    '''

    def __init__(self):
        '''reads in, stores, and sorts list of tasks to tasklist.txt'''
        self._user_tasklist = []
        task_file = open("tasklist.txt", "r")
        tasks = task_file.readlines()
        # appends tasks
        for line in tasks:
            current_task = line.strip().split(",")
            user_task = task.Task(current_task[0], current_task[1], current_task[2])
            self._user_tasklist.append(user_task)
        # sorts tasks
        self._user_tasklist = sorted(self._user_tasklist)

    def add_task(self, desc, date, time):
        '''adds task to tasklist and sorts the task according to due date and time'''
        # appends tasks (including the task description, due data, and time)
        self._user_tasklist.append(task.Task(desc, date, time))
        # sorts tasks by due date and time
        self._user_tasklist = sorted(self._user_tasklist)

    def mark_complete(self):
        '''marks the current task as completed by removing it from the tasklist'''

        self._user_tasklist.remove(self._user_tasklist[0])

    def save_file(self):
        '''writes the contents of the task list to the file and ends the program'''
        tasklist = open("tasklist.txt", "w")
        if len(self._user_tasklist) > 0:
            for num_objects in range(len(self._user_tasklist) - 1):
                tasklist.write(repr(self._user_tasklist[num_objects]) + "\n")
            tasklist.write(repr(self._user_tasklist[len(self._user_tasklist) - 1]))
            tasklist.close()

    def __len__(self):
        '''returns the length of the task list'''
        return len(self._user_tasklist)

    def get_current_task(self):
        '''returns first task object'''
        return self._user_tasklist[0]

    def __iter__(self):
        '''initializes the iterator attribute (n) and returns self'''
        self._n = -1
        return self

    def __next__(self):
        '''iterate the iterator one position at a time'''
        self._n += 1
        if self._n > len(self._user_tasklist) - 1:
            raise StopIteration
        else:
            return self._user_tasklist[self._n]