import platedecorator

class Stuffing(platedecorator.Platedecorator):
  '''Food Decoration; extend Plate Decorator'''

  def description(self):
    '''call superclass and additional description'''
    if super().count() == 0:
      return super().description() + "Stuffing"
    else:
      return super().description() + " and Stuffing"

  def area(self):
    '''call supperclass and substract food item's area (area = 18)'''
    return super().area() - 18

  def weight(self):
    '''call supperclass and substract food item's weight (area = 7)'''
    return super().weight() - 7

  def count(self):
    '''call superclass and add 1 to increment counter'''
    return super().count() + 1