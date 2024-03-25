#Creating of several different shapes according to the width and height input by the user
#2022/03/23
#Matthew Schramm
import math
def print_square():
    counter = 1
    box = ""
    for i in range(0,5):
        if counter == 1 or counter == 5:
            
            box += "* * * * *\n"
            counter += 1
            
        else:
            
            box += "*       *\n"
            counter += 1
    return box
  
def print_rectangle(width, height):
    for i in range(0,width):
        print("* ",end = "")
    for j in range(0,height-2):
        print()
        for z in range(0,width):
            
            if z == 0 or z == width-1:
                print("* ",end="")
            else:
                print("  ",end="")
        
    print()   
    for k in range(0,width):
        
        print("* ",end = "",sep = "")
    print()





def get_rectangle(width,height):
    rectangle = ""
    for i in range(0,width):
        rectangle += "* " 
    rectangle += "\n"
    for j in range(0,height-2):
        
        for z in range(0,width):
            
            if z == 0 :
                rectangle += "* "
            elif z == width-1:
                rectangle += "*"
                rectangle += "\n"
            
            else:
                rectangle += "  "
        
     
    for i in range(0,width):
        rectangle += "* "     
    return rectangle







