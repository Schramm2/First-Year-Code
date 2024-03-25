# Program that counts the number of pairs of consecutive characters in a string
# Matthew Schramm
# 28 april 2022
def pairs(message): #Function to count the pairs of consecutive characters
    
    
    
    counter2 = 0
    if len(message) == 0:
        return 0
    else:
        if message[counter2:counter2+1] == message[counter2 + 1:counter2 +2]:
            counter2 += 1
            return  counter2 + pairs(message[2:])
        else:
            return pairs(message[1:])
    
    

message = input("Enter a message: \n")
print("Number of pairs:",pairs(message))