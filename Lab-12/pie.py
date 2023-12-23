import platedecorator

class Pie(platedecorator.Platedecorator):
  '''Food Decoration; extend Plate Decorator'''

  def description(self):
    '''call superclass and additional description'''
    if super().count() == 0:
      return super().description() + "Pie"
    else:
      return super().description() + " and Pie"

  def area(self):
    '''call supperclass and substract food item's area (area = 19)'''
    return super().area() - 19

  def weight(self):
    '''call supperclass and substract food item's weight (area = 8)'''
    return super().weight() - 8

  def count(self):
    '''call superclass and add 1 to increment counter'''
    return super().count() + 1