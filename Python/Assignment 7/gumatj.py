# Functions for Gumatj calculations
# Matthew Schramm
# 16 april 2022
def decimal_to_gumatj(b): #Function to convert a decimal number to a gumatj number
    dec = ""
    if b > 0 and b < 5:
        dec = b
        return dec
    elif b > 4 and b <10:
        dec = b + 5
        return dec
    elif b >9 and b < 15:
        dec = b + 10
        return dec
    elif b >14 and b < 20:
        dec = b + 15
        return dec
    elif b >19 and b < 25:
        dec = b + 20
        return dec
    elif b > 24:
        for i in range(0 , 3):
            dec += str(b%5)
            b = b//5
        
        dec = dec[::-1]
        
        return dec
        
def gumatj_to_decimal(a): #Function to convert a gumatj number to a decimal number
    decimal = 0
    multiple = 1
    if a > 0 and a <5:
        return a
    else:
        gumatj = str(a)
        gumatj = gumatj[::-1]
        for i in range (0, len(gumatj)):
            decimal += int(gumatj[i]) * multiple
            multiple = multiple *5
            
        return decimal
            
def gumatj_add(a, b):#Function to add two gumatj numbers
    if a == 0 and b == 0:
        addGum = 0
    else:
        a = gumatj_to_decimal(a)
        b = gumatj_to_decimal(b)
        addGum = a + b
        addGum = decimal_to_gumatj(addGum)        
    
    return addGum



def gumatj_multiply(a, b): #Function to multiply two gumatj numbers
    multiplyGum = a * b
    if a == 0 or b == 0:
        multiplyGum = 0
    else:
        multiplyGum = decimal_to_gumatj(multiplyGum)
    
    return multiplyGum
        
    
    
        


