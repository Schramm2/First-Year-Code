# Program that determines if a given pattern matches a word
# Matthew Schramm
# 28 april 2022
def match(pattern, word): #Function to detemine if the pattern and a word are a match
    
    if pattern == "" and word == "":
        return -1
    elif pattern == "" or word == "":
        return -1
    elif pattern == word:
        return -1
    elif pattern == '*' and word == '':
        return True
    else:
        
            
        if pattern[0:1] == "?":
            if word[0:1].isalpha() == True:
                return match(pattern[1:] , word[1:])
            else:
                return match(pattern[1:] , word[1:])
        
        
        elif pattern[0:1] == "*" and pattern[1:2] == "*":
            if pattern[2:len(pattern)] in word:
                return match(pattern[2:] , word[2:]) 
            
        elif pattern[0:1] == "*" and "*" not in pattern[1:len(pattern)]:
            if pattern[1:len(pattern)] in word:
                return match(pattern[1:] , word[1:])
        
        
        
        elif pattern[0:1].isalpha() == True:
            if word[0:1] == pattern[0:1]:
                return match(pattern[1:] , word[1:])
            else:
                return match(pattern[1:] , word[1:])
            
