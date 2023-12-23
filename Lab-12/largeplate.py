import plate

class LargePlate(plate.Plate):
  '''Concrete Plate; extends Plate'''

  def description(self):
    '''returns description of plate'''
    return "Flimsy 12 inch paper plate with "

  def area(self):
    '''area = 113 square inches'''
    return 113

  def weight(self):
    '''weight = 24 ounces'''
    return 24

  def count(self):
    '''count = 0, no items on the plate yet'''
    return 0