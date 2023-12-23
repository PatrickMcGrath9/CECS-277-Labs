class Task:
  ''' Displays and holds information of a task
  Attributes:
    desc (string): A description of the task
    date (string): Due date of the task
    time (string): The time at which the task is due
  '''

  def __init__(self, desc, date, time):
    '''initializes desc, date, and time'''
    self._desc = desc
    self._date = date
    self._time = time

  def date(self):
    return self._date

  def __str__(self):
    '''returns a string that contains the task's description, date, and
    time'''
    task_info = self._desc + " - Due: " + self._date + " at " + self._time
    return task_info

  def __repr__(self):
    '''returns a string that contains the task's description, date, and
    time which is meant to be written to a file'''
    return f"{self._desc},{self._date},{self._time}"

  def __lt__(self, other):
    '''compares two tasks' dates, times, and descriptions with the < operator
    and returns true if the current task should be first '''
    years_one = self._date[6:]
    years_two = other._date[6:]

    months_one = self._date[0:2]
    months_two = other._date[0:2]

    days_one = self._date[3:5]
    days_two = other._date[3:5]

    hours_one = self._time[0:2]
    hours_two = other._time[0:2]

    minutes_one = self._time[3:]
    minutes_two = other._time[3:]

    if years_one < years_two:
      return True

    elif years_one == years_two:

      if months_one < months_two:
        return True

      elif months_one == months_two:

        if days_one < days_two:
          return True

        elif days_one == days_two:

          if hours_one < hours_two:
            return True

          elif hours_one == hours_two:

            if minutes_one < minutes_two:
              return True

            elif minutes_one == minutes_two:

              if self.desc < other.desc:
                return True

              else:
                return False

            else:
              return False

          else:
            return False

        else:
          return False

      else:
        return False

    else:
      return False