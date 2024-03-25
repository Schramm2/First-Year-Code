
  

def check_lost (grid):
  
  """return True if there are no 0 values and there are no
  adjacent values that are equal; otherwise False""" 
  value = False
  for z in range(0,4):
    
    
    for i in range(len(grid[z])-1):
      if grid[z][i] == 0:
        return value
      else:
        
        if grid[z][i] == grid[z][i+1]:
          for z in range(0,4):
          
          
            for i in range(len(grid[z])-1):
              if grid[z][i] == 0:
                value = True
                return value
              else:
                return value
        
        
        elif grid[z][i] == 0:
          for z in range(0,4):
          
          
            for i in range(len(grid[z])-1):
              if grid[z][i] == grid[z][i+1]:
                value = True
                return value
              else:
                return value
      
            
