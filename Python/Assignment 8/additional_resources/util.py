# Module to create the functions to run the program testutil
# Matthew Schramm
# 21 april 2022
import copy
def create_grid(grid):
  """create a 4x4 array of zeroes within grid"""
  for r in range(0,4):
    
      grid.append([0 for c in range(0,4)])
    
  
  return grid
 
 
 
  
  
 
def print_grid (grid):
  """print out a 4x4 grid in 5-width columns within a box"""
  printGrid = ""
  print("+",end = "" , sep = "")
  for i in range(0, 20):
    print("-", end = "", sep = "")
  print("+")
  for z in range(0,4):
    
    print("|",end = "", sep = "")
    for i in range(len(grid[z])):
      if grid[z][i] == 0:
        print("     ",end = "", sep = "")
      else:
        print(grid[z][i],end = "", sep = "") 
        for x in range(0,4 - len(str(grid[z][i]))+1):
          print(" " ,end = "", sep = "")
              
    print("|\n",end = "", sep = "")            
  
  print("+",end = "" , sep = "")
  for i in range(0, 20):
    print("-", end = "", sep = "")
  print("+")
  

  

def check_lost (grid):
  
  """return True if there are no 0 values and there are no
  adjacent values that are equal; otherwise False""" 
 
  for z in range(0,4):
    
    
    
    for i in range(len(grid[z])):
      if grid[z][i] == 0:
        return False
  
  for x in range(0,4):
    
    
    
    for g in range(len(grid[z])-1):
      if grid[x][g] == grid[x][g+1]:
        return False      
  return True
         
        
        
        
          
    
def check_won (grid):
  """return True if a value>=32 is found in the grid; otherwise 
  False"""
  for z in range(0,4):
    
    
    for i in range(len(grid[z])):
      if grid[z][i] >= 32:
        return True
      
  return False

def copy_grid (grid):
  """return a copy of the given grid"""
  grid2 = copy.deepcopy(grid)
  
  return grid2
  
  

def grid_equal (grid1, grid2):
  """check if 2 grids are equal - return boolean value"""
  if grid1 == grid2:
    return True
  else:
    return False