word = "Habits"
guess = input("What is your guess?\n")
res = ""
guess = guess.upper()
    
print("[",guess,"]",sep = "")
    
for i in range(len(word)):
    if guess[i] == word[i]:
        res += "*"
    elif guess[i] in word:
        res += "+"
    else:
        res += "-"
                        
        
        
            
        
        
        
        