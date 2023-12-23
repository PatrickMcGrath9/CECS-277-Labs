import plate

class SmallPlate(plate.Plate):
  '''Concrete Plate; extends Plate'''

  def description(self):
    '''returns description of plate'''
    return "Sturdy 10 inch paper plate with "

  def area(self):
    '''area = 78 square inches'''
    return 78

  def weight(self):
    '''weight = 32 ounces'''
    return 32

  def count(self):
    '''count = 0, no items on the plate yet'''
    return 0