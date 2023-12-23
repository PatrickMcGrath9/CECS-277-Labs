class Rectangle:

  def __init__(self, w, h):    
    '''sets attributes, passes in w and h for width and height, sets x and y to 0'''
    self.width = w           
    self.height = h          
    self.x_coord = 0               
    self.y_coord = 0               

  def get_coords(self):
    '''returns x and y values as a pair'''
    coords_list = [self.x_coord, self.y_coord]
    return coords_list                              

  def get_dimensions(self):
    '''returns width and height as a pair'''
    dimensions_list = [self.width, self.height]
    return dimensions_list                          

  def move_up(self):
    '''moves the rectangle up one row'''
    self.y_coord -= 1             
    
  def move_down(self):
    '''moves the rectangle down one row'''
    self.y_coord += 1             

  def move_left(self):
    '''moves the rectangle left one column'''
    self.x_coord -= 1             

  def move_right(self):
    '''moves the rectangle right one column'''
    self.x_coord += 1             