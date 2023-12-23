import platedecorator

class Potatoes(platedecorator.Platedecorator):
  '''Food Decoration; extend Plate Decorator'''

  def description(self):
    '''call superclass and additional description'''
    if super().count() == 0:
      return super().description() + "Potatoes"
    else:
      return super().description() + " and Potatoes"

  def area(self):
    '''call supperclass and substract food item's area (area = 18)'''
    return super().area() - 18

  def weight(self):
    '''call supperclass and substract food item's weight (area = 6)'''
    return super().weight() - 6

  def count(self):
    '''call superclass and add 1 to increment counter'''
    return super().count() + 1