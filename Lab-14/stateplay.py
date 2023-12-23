import puppystate
import stateasleep

class StatePlay(puppystate.PuppyState):
  '''puppy in "play" state'''

  def feed(self, puppy):
    '''puppy does not go back to eating state from playing state'''
    return ("The puppy is too busy playing with the ball to eat right now.")

  def play(self, puppy):
    '''puppy plays with ball up to 3 times; at third time, puppy falls asleep'''
    if puppy.plays < 2:
      puppy.inc_plays()
      return ("The throw the ball again and the puppy excitedly chases it.")
    else:
      puppy.change_state(stateasleep.StateAsleep())   # change to sleep state
      puppy.reset()                                   # when puppy falls asleep, reset counter
      return (f"The throw the ball again and the puppy excitedly chases it.\nThe puppy played so much it fell asleep!")