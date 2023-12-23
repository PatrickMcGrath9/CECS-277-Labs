import platedecorator

class Turkey(platedecorator.Platedecorator):
  '''Food Decoration; extend Plate Decorator'''

  def description(self):
    '''call superclass and additional description'''
    if super().count() == 0:
      return super().description() + "Turkey"
    else:
      return super().description() + " and Turkey"

  def area(self):
    '''call supperclass and substract food item's area (area = 15)'''
    return super().area() - 15

  def weight(self):
    '''call superclass and substract food item's weight (area = 4)'''
    return super().weight() - 4

  def count(self):
    '''call superclass and add 1 to increment counter'''
    return super().count() + 1