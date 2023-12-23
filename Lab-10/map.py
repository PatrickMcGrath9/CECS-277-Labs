class Map:
  '''Singleton
      Attributes:
        _map - actual map text
        _revealed - corresponds with displaying map text or hiding it'''
  _instance = None
  _initialized = False

  def __new__(cls):
    '''if the map hasn’t been constructed, then construct it and store it in
the instance class variable and return it. If it has, then just return the instance'''
    if cls._instance is None:
      cls._instance = super().__new__(cls)
    return cls._instance


  def __init__(self):
    '''create and fill the 2D map list from the file contents; contents of file are 
    stored; revealed list is used to determine whether the contents of the map are 
    displayed or not'''
    if not Map._initialized:
      file = open("map.txt")
      self._map = []
      for row in file:
        list = []
        for item in row:
          if item != '\n':
            list.append(item)
        self._map.append(list)
      file.close()
      
      self._revealed = []
      for row in self._map:
        list = []
        for item in row:
          list.append(False)
        self._revealed.append(list)
      Map._initialized = True
  
  def __getitem__(self, row):
    '''returns row from the map'''
    return self._map[row]


  def __len__(self):
    '''returns number of rows in the map list'''
    return len(self._map)


  def show_map(self, loc):
    '''returns the map as a string in the format of a 5x5 matrix of
characters'''
    map_string = ''
    for row in range(len(self._map)):
        for column in range(len(self._map[row])):
            if loc[0] == row and loc[1] == column:
                map_string += '* '
            elif self._revealed[row][column]:
                map_string += self._map[row][column] + ' '
            else:
                map_string += 'x '
        map_string += '\n'
    return map_string


  def reveal(self, loc):
    '''sets the value in the 2D revealed list at the specified location to True'''
    self._revealed[loc[0]][loc[1]] = True


  def remove_at_loc(self, loc):
    '''overwrites the character in the map list at the specified
location with an ‘n’'''
    self._map[loc[0]][loc[1]] = 'n'