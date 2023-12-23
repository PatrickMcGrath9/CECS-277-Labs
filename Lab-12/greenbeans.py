import platedecorator

class GreenBeans(platedecorator.Platedecorator):
  '''Food Decoration; extend Plate Decorator'''

  def description(self):
    '''call superclass and additional description'''
    if super().count() == 0:
      return super().description() + "Green Beans"
    else:
      return super().description() + " and Green Beans"

  def area(self):
    '''call supperclass and substract food item's area (area = 20)'''
    return super().area() - 20

  def weight(self):
    '''call supperclass and substract food item's weight (area = 3)'''
    return super().weight() - 3

  def count(self):
    '''call superclass and add 1 to increment counter'''
    return super().count() + 1