# When the wildcard character ‘?’ appears in a pattern it indicates that any letter may appear at that position.
# When the wildcard character ‘*’ appears in a pattern it indicates that a sequence of zero or more of letters is acceptable at that position.
# When a letter appears in a pattern it indicates that precisely that letter must appear at the same position in matching words. 
# Program that is used to determine if a given pattern matches a given word
# Matthew Schramm
# 28 april 2022
def match(pattern, word): #Function to detemine if the pattern and a word are a match
    if pattern == " " and word == " ":
        return -1
    elif pattern == " " or word == " ":
        return -1
    elif pattern == word:
        return -1
    else:
        if "?" not in pattern and "*" not in pattern:
            if pattern == word:
                return True
        elif pattern[0:1] == "?":
            if word[0:1].isalpha() == True:
                return match(pattern[1:] , word[1:])
        elif pattern[0:1] == "*":
            if word[0:word.find(pattern[1:2])].isalpha() == True:
                return match(pattern[1:] , word[1:])
        elif pattern[0:1].isalpha() == True:
            if word[0:1] == pattern[0:1]:
                return match(pattern[1:] , word[1:])
            
            