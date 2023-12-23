import puppystate
import stateeat

class StateAsleep(puppystate.PuppyState):
  '''puppy in "asleep" state'''

  def feed(self, puppy):
    '''puppy wakes up to "feed" option'''
    puppy.inc_feeds()
    puppy.change_state(stateeat.StateEat())   # change to eat state
    return ("The puppy wakes up and comes running to eat.")

  def play(self, puppy):
    '''puppy does not wake up "play" option'''
    return ("The puppy is asleep. It doesn't want to play right now.")