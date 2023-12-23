import puppystate
import stateplay
import stateasleep

class StateEat(puppystate.PuppyState):
  '''puppy in "eat" state'''

  def feed(self, puppy):
    '''puppy eats up to 3 times; at third time, puppy falls asleep'''
    if puppy.feeds < 2:
      puppy.inc_feeds()
      return ("The puppy continues to eat as you add another scoop of kibble to its bowl.")
    else:
      puppy.change_state(stateasleep.StateAsleep())   # change to sleep state
      puppy.reset()                                   # when puppy falls asleep, reset counter
      return (f"The puppy continues to eat as you add another scoop of kibble to its bowl.\nThe puppy ate so much it fell asleep!")

  def play(self, puppy):
    '''puppy can go from eating state to play state'''
    puppy.inc_plays()
    puppy.change_state(stateplay.StatePlay())         # change to play state
    return ("The puppy looks up from its food and chases the ball you threw.")