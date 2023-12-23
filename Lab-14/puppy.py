
import stateasleep

class Puppy:
  '''the object the user interacts with'''

  def __init__(self):
    '''initialize state to asleep state; play and feed initialized to 0'''
    self._plays = 0
    self._feeds = 0
    self._state = stateasleep.StateAsleep()


  @property
  def plays(self):
    '''property for plays'''
    return self._plays

  @property
  def feeds(self):
    '''property for feeds'''
    return self._feeds

  def change_state(self, new_state):
    '''updates puppy's state to new state'''
    self._state = new_state

  def throw_ball(self):
    '''calls play method for whichever state the puppy is in'''
    return self._state.play(self)

  def give_food(self):
    '''calls feed method for whichever state the puppy is in'''
    return self._state.feed(self)

  def inc_feeds(self):
    '''increments feeds by 1'''
    self._feeds += 1

  def inc_plays(self):
    '''increments plays by 1'''
    self._plays += 1

  def reset(self):
    '''reinitializes feeds and plays attributes'''
    self._feeds = 0
    self._plays = 0