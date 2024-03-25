#Program to calculate the amount of time the factorial of a number is performed
#2022/03/23
#Matthew Schramm
def get_integer(s):
    if s == "n":
        s = input("Enter n:\n")
        s = int(s)    
        return s
    elif s == "k":
        s = input("Enter k:\n")
        s = int(s)    
        return s
    else:
        s = input("Enter number:\n")
        s = int(s)
        return s
    
    
    

def calc_factorial(n):
    
    nfactorial = 1
    for i in range (1, n+1):
        nfactorial *= i  
        
    return nfactorial
        
    
    
   