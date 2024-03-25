wFile = open("EnglishWords.txt","r")
words = wFile.readlines()[60:]
wFile.close()
print("***** Anagram Set Search *****")
wrdlength = eval(input("Enter word length: \n"))
print("Searching...")
fileName = input("Enter file name: \n")
print("Writing Results...")

counter1 = 0
for word in words:
    if "\n" in word:
        words[counter1] = words[counter1].replace('\n','')
        counter1+= 1

counter2 = 0
anaLength = []
for word1 in words:
    if len(word1) == wrdlength:
        
        anaLength.append(words[counter2])
        counter2 += 1
    else:
        counter2 += 1
        

fName = fileName
f = open(fName,"w")
anaLengthEqual = []
anagramComplete = [[]]


for word2 in anaLength:
    
    for word3 in anaLength:
        
        if sorted(word2) == sorted(word3) and word2 != word3 and word2 not in anaLengthEqual and :
            
            anaLengthEqual.append(word2)
            anaLengthEqual.append(word3)
        
    
    if anaLengthEqual != []:
        anaLengthEqual = sorted(anaLengthEqual)                       
                
                
        print(anaLengthEqual, file = f)                
        anaLengthEqual = []
    else:
        anaLengthEqual = []
        



f.close()       




    

    


            
        
            
          
            
   
 
         

