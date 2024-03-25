#Text-based Graph creator
#2022/03/23
#Matthew Schramm
import math

function = input("Enter a function f(x):\n")

if function[2:len(function)] != "":
    change = function[2:len(function)]
    change = int(change)  
    

    

sign = function[1:2]



   

for j in range(-10,11,1):
    
    if j == 0:
        if sign == "+":
            j=j+change
            for i in range(-10,11,1):
                if i == 0:
                    print("+", end = "")
                elif i == j*-1:
                    print("o", end = "")
                else:
                    print("-", end = "")       
        elif sign == "-":
            j=j-change
            for i in range(-10,11,1):
                if i == 0:
                    
                    print("+", end = "")
                elif i == j*-1:
                    print("o", end = "")
                else:
                    print("-", end = "")    
        elif sign == "":
            
            for i in range(-10,11,1):
                if i == 0:
                    
                    print("o", end = "")
                elif i == j*-1:
                    print("o", end = "")
                else:
                    print("-", end = "")               
            
            
        print()
    else:
        if sign == "+":
            j=j+change
            for i in range(-10,11,1):
                if i == 0:
                    if i == j*-1:
                        print("o", end = "")
                    else:
                        print("|", end = "")
                elif i == j*-1:
                    print("o", end = "")
                else:
                    print(" ", end = "")
        elif sign == "-":
            j=j-change
            for i in range(-10,11,1):
                if i == 0:
                    if i == j*-1:
                        print("o", end = "")
                    else:
                        print("|", end = "")
                    
                elif i == j*-1:
                    print("o", end = "")
                else:
                    print(" ", end = "") 
        elif sign == "":
            j=j
            for i in range(-10,11,1):
                if i == 0:
                    if i == j*-1:
                        print("o", end = "")
                    else:
                        print("|", end = "")
                    
                elif i == j*-1:
                    print("o", end = "")
                else:
                    print(" ", end = "")   
        print()    
            
            
                
        
   

    

    
        
    
    