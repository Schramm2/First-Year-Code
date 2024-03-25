import os.path

print("***** Anagram Finder *****")
if os.path.isfile("EnglishWords.txt"):
    
    wordAnagram = input("Enter a word: ")
    myFile = open("EnglishWords.txt","r")
    words = myFile.readlines()[60:]
    counter1 = 0
    for word in words:
        if "\n" in word:
            words[counter1] = words[counter1].replace('\n','')
            counter1+= 1
    
    
    
    
    anagrams = []
    counter2 = 0
    for word in words:
        if word == wordAnagram:
            counter2+= 1
        
        
        elif sorted(wordAnagram) == sorted(word):
            anagrams.append(words[counter2])
            counter2+=1
        else:
            counter2+=1
    if anagrams == []:
        print("\nSorry, anagrams of '",wordAnagram,"' could not be found.",sep = "")
    else:
        print("\n",sorted(anagrams),sep = "")
    
        
        
else:
    print("Sorry, could not find file 'EnglishWords.txt'.")    

